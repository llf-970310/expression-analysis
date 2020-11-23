class ReportConfig(object):
    structure_list = ['sum-aspects', 'aspects', 'example', 'opinion', 'sum']
    logic_list = ['cause-affect', 'transition', 'progressive', 'parallel']

    hit_dict = {
        'sum-aspects': '你在表达时，很好的使用了分层法。分层法是有一种经典的表达方法，也就是我们平时说的总-分结构，它将观点层层剥离，'
                       '是讲述内容更有层次性。自上而下、现总结后具体的表达顺序，能够提前说明你叙述内容之间的逻辑关系，让倾听者对内容做出与你相同的理解。',
        'aspects': '你在交流中，能将内容进行有逻辑的组织。利用分点，将你的观点进行拆分讲解，相信你在平时工作、生活和学习的表达中，也是一名思路清晰，有条理的表达者。',
        'example': '在表达时，合理的使用了举例。例子是表达力必不可少的的元素，它能支撑或强调表达者的观点，增强说服力。',
        'opinion': '在表达时，你能够将自己的观点进行浓缩，用简洁、有力的语言表达自己的观点，让人印象深刻。',
        'sum': '在表达时，你会有意识的在结束进行一个总的回顾，这种前后呼应的表达方式，它能再次强化你的观点，突出内容的重点，加深别人对你的印象。'
               '自下而上的思考，能让你在思考、设计交流内容时，充分完善你的思路，以有效的组织思想的方式，让对方立刻理解你想要表达的信息。'
    }
    not_hit_dict = {
        'sum-aspects': '在表达你的观点，或者进行发言时，你可以适当的使用分层法。分层法是有一种经典的表达方法，'
                       '也就是我们平时说的总-分结构，它将观点层层剥离，是讲述内容更有层次性。',
        'aspects': '在论述复杂话题时，利用分点，将你的观点进行拆分讲解，能让你的表达更清晰。',
        'example': '在表达观点时，你可以适当的使用举例，来证明你的观点。例子是表达力必不可少的的元素，它能支撑或强调表达者的观点，增强说服力。',
        'opinion': '表达中，亮明观点，用简洁、有力的语言表达自己的观点，能够让人印象更深刻。',
        'sum': '当结束活临近话题结尾时，有意识的在结束进行一个总的回顾，这种前后呼应的表达方式，它能再次强化你的观点，突出内容的重点，加深别人对你的印象。'
    }


class MongoConfig:
    host = '106.13.160.74'
    port = 27017
    auth = 'SCRAM-SHA-1'  # auth mechanism, set to None if auth is not needed
    user = 'iselab'
    password = 'iselab###nju.cn'
    db = 'expression'

    current = 'current'
    questions = 'questions'
    api_accounts = 'api_accounts'
    users = 'users'
    history = 'history'
    analysis = 'analysis'
    wav_test = 'wav_test'


# -------------- UAAM CONFIG --------------
INTERVAL_TIME_THRESHOLD1 = 0.7  # 第一种题型的间隔时间阈值
SEGMENTS_VOLUME1 = 3  # 第一种题型计算音量时分的段数
INTERVAL_TIME_THRESHOLD2 = 2.0  # 第二种题型的间隔时间阈值
SEGMENTS_RCG1 = 1  # 第一种识别时分的段数
SEGMENTS_RCG2 = 1  # 第二种识别时分的段数
SEGMENTS_VOLUME2 = 3  # 第二种题型计算音量时分的段数
INTERVAL_TIME_THRESHOLD3 = 2.0  # 第三种题型的间隔时间阈值
SEGMENTS_RCG3 = 3  # 第三种识别时分的段数
SEGMENTS_VOLUME3 = 3  # 第三种题型计算音量时分的段数
MAIN_IDEA_WORD_COUNT = 30  # 计算主旨关键词是否在前面说到时所用的字数

# -------- RCG --------
RCG_MAX_RETRY = 3


# XUNFEI API interface
XF_RCG_URL = 'https://api.xfyun.cn/v1/service/v1/iat'
XF_EVL_URL = 'https://api.xfyun.cn/v1/service/v1/ise'

XF_EVL_CATEGORY = "read_chapter"
# rcg_param
XF_RCG_ENGINE_TYPE = "sms8k"

# -------- ACCOUNTS --------
XF_EVL_APP_ID = '5b482315'  # Ordinary account
XF_EVL_API_KEY = 'd5eabc8c4a8ea2edb03f8e486d7076b3'
XF_RCG_APP_ID = '5b482315'
XF_RCG_API_KEY = '33d2e52fe4bdddae35e09026f2167867'

BD_RCG_APP_ID = '17806567' # parclab.com注册的百度账号
BD_RCG_API_KEY = '4AEOoAjSupTpev4pLz72SI2M'
BD_RCG_SECRET_KEY = 'dUdOlfNGPG1kERSBwhqRuo6QnMTX32ME'

BD_BOS_AK = '6ff21a46abcf4fa2828478d337f4f91b'  # parclab
BD_BOS_SK = 'a244696b2607431090b4a0e7f5c0947a'
BD_BOS_HOST = 'su.bcebos.com'
BD_BOS_BUCKET = 'bos-parclab-exp'
# --------------------------
