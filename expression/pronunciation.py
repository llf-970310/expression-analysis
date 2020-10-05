# -*— coding: utf-8 -*-
# Time    : 2018/10/16 下午1:04
# Author  : tangdaye
# Desc    : 探索语音相似度
from pypinyin import lazy_pinyin
from zhon.hanzi import punctuation

# import xlrd

alpha, beta = 1, 1  # 分别代表声母和韵母在计算中的权重
similar_threshold = 0.2  # 相似度阈值
# 声母表
consonants = (
    'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's', 'y',
    'w')
# 韵母表
vowels = (
    'a', 'o', 'e', 'i', 'u', 'v', 'ai', 'ei', 'ui', 'ao', 'ou', 'iu', 'ie', 'ue', 'er', 'an', 'en', 'in', 'un', 'ang',
    'eng', 'ing', 'ong', 'ia', 'ua', 'uo', 'uai', 'uan', 'ian', 'iao', 'iang', 'uang', 'iong')
# 单独成字韵母表
vowel_word = ('a', 'o', 'e', 'ai', 'ei', 'ao', 'ou', 'er', 'an', 'en')
# 声母距离：基于声母表
consonant_destination = [
    [0.0, 0.3, 0.3, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.3, 0.0, 0.3, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.3, 0.3, 0.0, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.3, 0.3, 0.3, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.0, 0.3, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.3, 0.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.0, 0.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.1, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.4, 0.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.4, 0.0, 0.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.4, 1.0, 1.0, 1.0, 1.0, 0.4, 0.4, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.3, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 0.0, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 0.3, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.3, 0.3, 0.5, 0.2, 0.4, 0.4, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 0.0, 0.3, 0.5, 0.4, 0.2, 0.4, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 0.3, 0.0, 0.5, 0.4, 0.4, 0.2, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.0, 0.7, 0.7, 0.7, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.2, 0.4, 0.4, 0.7, 0.0, 0.3, 0.3, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.4, 0.2, 0.4, 0.7, 0.3, 0.0, 0.3, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.4, 0.4, 0.2, 0.7, 0.3, 0.3, 0.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 0.7, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0]
]
# 韵母距离：基于韵母表
vowel_destination = [
    [0.0, 0.7, 0.6, 1.0, 1.0, 1.0, 0.5, 0.8, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8, 1.0, 1.0, 1.0, 0.9, 1.0, 1.0, 1.0,
     0.1, 0.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.7, 0.0, 0.7, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 0.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.6, 0.7, 0.0, 1.0, 1.0, 1.0, 1.0, 0.4, 1.0, 1.0, 1.0, 1.0, 0.8, 0.9, 0.3, 1.0, 0.7, 1.0, 1.0, 1.0, 0.8, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.9, 1.0, 1.0, 0.9, 0.5, 0.6, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 0.8, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.7, 1.0, 1.0, 0.0, 0.3, 1.0, 1.0, 0.7, 1.0, 0.7, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.3, 0.0, 1.0, 1.0, 0.8, 1.0, 1.0, 0.8, 1.0, 0.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.5, 1.0, 1.0, 0.9, 1.0, 1.0, 0.0, 0.3, 0.8, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 0.9, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 0.2, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.8, 1.0, 0.4, 0.9, 1.0, 1.0, 0.3, 0.0, 0.7, 1.0, 1.0, 1.0, 0.9, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.9, 0.7, 0.8, 0.8, 0.7, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0, 1.0, 1.0],
    [1.0, 0.6, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.9, 0.8, 0.8, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 0.7, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 0.8, 0.5, 1.0, 1.0, 1.0, 0.9, 1.0, 1.0, 1.0, 0.7, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     0.5, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 0.9, 0.6, 1.0, 0.6, 1.0, 0.8, 1.0, 1.0, 1.0, 0.9, 0.5, 0.0, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.7, 1.0, 0.3, 0.5, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 0.3, 0.3, 0.5, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 0.0, 1.0, 0.5, 1.0, 0.1, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.1, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 0.3, 0.5, 1.0, 0.0, 1.0, 1.0, 1.0, 0.9,
     1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.7, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 0.7, 0.7, 1.0, 0.3, 0.3, 1.0],
    [1.0, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.3, 1.0, 1.0, 0.7, 0.0, 1.0, 0.7,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.1, 1.0, 1.0, 1.0, 0.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9, 1.0, 0.7, 1.0, 0.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3],
    [0.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     0.0, 0.5, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0],
    [0.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     0.5, 0.0, 0.7, 0.7, 0.7, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.2, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 0.6, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0, 1.0,
     1.0, 0.7, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     1.0, 0.7, 1.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0,
     1.0, 0.7, 1.0, 0.5, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.7, 1.0, 1.0, 1.0,
     0.7, 1.0, 1.0, 1.0, 0.5, 0.0, 1.0, 0.7, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.7, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0, 0.7, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 0.7, 0.7, 0.0, 0.3, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 1.0, 1.0, 1.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0]]
# 单独成字韵母与音节距离：基于声母表和单独成字韵母表
consonant_vowel_destination = [
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.9, 1.0, 0.9, 0.9, 0.9, 0.9, 0.9, 1.0, 0.9, 0.9],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5]
]


def is_pinyin(pinyin):
    if pinyin[:1] not in consonants:
        if pinyin[:2] not in consonants:
            if pinyin not in vowel_word:
                return False
    return True


def change_into_pinyin(sentence):
    return [word for word in lazy_pinyin(sentence) if word not in punctuation]


def consonant_and_vowel(pinyin):
    if pinyin[:2] in consonants:
        if pinyin[2:] in vowels:
            return pinyin[:2], pinyin[2:]
        else:
            raise Exception('pinyin error')
    elif pinyin[:1] in consonants:
        if pinyin[1:] in vowels:
            return pinyin[:1], pinyin[1:]
        else:
            raise Exception('pinyin error')
    elif pinyin in vowel_word:
        return '', pinyin
    else:
        raise Exception('pinyin error')


def destination(pinyin1, pinyin2):
    # pinyin1, pinyin2 = lazy_pinyin(character1)[0], lazy_pinyin(character2)[0]
    # if not is_pinyin(pinyin1):
    #     if not is_pinyin(pinyin2):
    #         return 0 if pinyin1 == pinyin2 else 1
    #     else:
    #         return 1
    # else:
    #     if not is_pinyin(pinyin2):
    #         return 1
    consonant1, vowel1 = consonant_and_vowel(pinyin1)
    consonant2, vowel2 = consonant_and_vowel(pinyin2)
    if consonant1 and consonant2:
        consonant_dest = consonant_destination[consonants.index(consonant1)][consonants.index(consonant2)]
        vowel_dest = vowel_destination[vowels.index(vowel1)][vowels.index(vowel2)]
        # 加权算数平均
        return (alpha * consonant_dest + beta * vowel_dest) / (alpha + beta)
    elif not consonant1 and consonant2:
        consonant_dest = consonant_vowel_destination[consonants.index(consonant2)][vowel_word.index(vowel1)]
        vowel_dest = vowel_destination[vowels.index(vowel1)][vowels.index(vowel2)]
        # 加权算数平均
        return (alpha * consonant_dest + beta * vowel_dest) / (alpha + beta)
    elif not consonant2 and consonant1:
        consonant_dest = consonant_vowel_destination[consonants.index(consonant1)][vowel_word.index(vowel2)]
        vowel_dest = vowel_destination[vowels.index(vowel1)][vowels.index(vowel2)]
        # 加权算数平均
        return (alpha * consonant_dest + beta * vowel_dest) / (alpha + beta)
    else:
        return vowel_destination[vowels.index(vowel1)][vowels.index(vowel2)] / 2


def check():
    for i in range(33):
        for j in range(i, 33):
            if not consonant_destination[i][j] == consonant_destination[j][i]:
                return i, j
    return True


def similar_pronunciation(word1, word2):
    if not len(word1) == len(word2):
        return False
    else:
        sim = 0
        for i in range(len(word1)):
            temp = destination(word1[i], word2[i])
            sim = sim + temp
        return sim / len(word1) <= similar_threshold


def in_pronunciation(word, sentence):
    sentence_pinyin = change_into_pinyin(sentence)
    word_pinyin = change_into_pinyin(word)
    len_sentence, len_word = len(sentence_pinyin), len(word_pinyin)
    if len_sentence < len_word:
        return False
    else:
        for i in range(len_sentence - len_word + 1):
            temp = sentence_pinyin[i:i + len_word]
            try:
                if similar_pronunciation(word_pinyin, temp):
                    return True
            except Exception:
                continue
        return False


# def write_excel_into_file():
#     excel_file = xlrd.open_workbook(r'source/汉语拼音距离.xlsx')
#     string = '韵母距离\n'
#     sheet0 = excel_file.sheet_by_index(0)
#     list0 = []
#     for i in range(1, 34):
#         temp = []
#         for j in range(1, 34):
#             temp.append(float(sheet0.cell(i, j).value))
#         list0.append(temp)
#     string += list0.__str__() + '\n\n声母距离\n'
#     sheet1 = excel_file.sheet_by_index(1)
#     list1 = []
#     for i in range(1, 23):
#         temp = []
#         for j in range(1, 23):
#             temp.append(float(sheet1.cell(i, j).value))
#         list1.append(temp)
#     string += list1.__str__() + '\n\n单独成字与声母距离\n'
#     sheet2 = excel_file.sheet_by_index(2)
#     list2 = []
#     for i in range(1, 24):
#         temp = []
#         for j in range(1, 11):
#             temp.append(float(sheet2.cell(i, j).value))
#         list2.append(temp)
#     string += list2.__str__()
#
#     string = string.replace('],', '],\n')
#     with open('pro.txt', 'w') as f:
#         f.write(string)


if __name__ == '__main__':
    x = '这道题说的是中国的沿海地区，经济发达地区面临电力短缺的问题，比如说像上海北京。及时行乐限电措施，安徽有470家企业，7月份以来' \
        '也被限制停电，另外就是中国电网说了啊长沙。老地区的确是严重缺电的，而根据剑桥能源署的饿数据显示中国有10%的电力短缺很严重。'
    print(in_pronunciation('7月', x))
    # write_excel_into_file()
    # print(consonant_destination[11][21],consonant_destination[21][11])
    # print(in_pronunciation('高铁', '中国糕点十分出名'))
    # print(len(vowel_destination[4]))
    # print(change_into_pinyin('今天天气很好，很晴朗。'))
# print(consonant_and_vowel('xiong'))
