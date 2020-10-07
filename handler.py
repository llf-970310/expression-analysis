import json
import logging
import traceback
import analysis_features
import analysis_scores
from analysis.ttypes import *
from errors import *
from utils_file import get_wav_file_bytes_io


def analyze_reading_question(request: AnalyzeReadingQuestionRequest) -> AnalyzeReadingQuestionResponse:
    resp = AnalyzeReadingQuestionResponse()

    file_path = request.filePath
    std_text = request.stdText

    if file_path == "" or file_path is None:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        file = get_wav_file_bytes_io(file_path, "bos")
        if file is not None:
            feature = analysis_features.analysis1(file, std_text)
            score = analysis_scores.score1(feature, rcg_interface='baidu')

            resp.feature = json.dumps(feature)
            resp.qualityScore = score["quality"]
            fill_status_of_resp(resp)
        else:
            logging.error('Finally failed to get audio file from bos after retries.')

    except Exception as e:
        tr = traceback.format_exc() + "\naudio:" + file_path + "\nfile_location: bos"
        print(tr)
        logging.error('error happened during process task: %s' % e)

        resp.statusCode = -1
        resp.statusMsg = str(e)

    return resp


def analyze_retelling_question(request: AnalyzeRetellingQuestionRequest) -> AnalyzeRetellingQuestionResponse:
    resp = AnalyzeRetellingQuestionResponse()

    file_path = request.filePath
    keywords = request.keywords
    detailwords = request.detailwords
    key_weights = request.keyWeights
    detail_weights = request.detailWeights

    if file_path == "" or file_path is None \
            or keywords is None or detailwords is None \
            or key_weights is None or detail_weights is None:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        file = get_wav_file_bytes_io(file_path, "bos")
        if file is not None:
            feature = analysis_features.analysis2(file, keywords, detailwords)
            score = analysis_scores.score2(feature['key_hits'], feature['detail_hits'], key_weights, detail_weights)

            resp.feature = json.dumps(feature)
            resp.keyScore = score["key"]
            resp.detailScore = score["detail"]
            fill_status_of_resp(resp)
        else:
            logging.error('Finally failed to get audio file from bos after retries.')

    except Exception as e:
        tr = traceback.format_exc() + "\naudio:" + file_path + "\nfile_location: bos"
        print(tr)
        logging.error('error happened during process task: %s' % e)

        resp.statusCode = -1
        resp.statusMsg = str(e)

    return resp


def analyze_expression_question(request: AnalyzeExpressionQuestionRequest) -> AnalyzeExpressionQuestionResponse:
    resp = AnalyzeExpressionQuestionResponse()

    file_path = request.filePath
    wordbase = request.wordbase

    if file_path == "" or wordbase is None:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        file = get_wav_file_bytes_io(file_path, "bos")
        if file is not None:
            feature = analysis_features.analysis3(file, wordbase, timeout=30)
            score = analysis_scores.score3(feature)

            resp.feature = json.dumps(feature)
            resp.structureScore = score["structure"]
            resp.logicScore = score["logic"]
            fill_status_of_resp(resp)
        else:
            logging.error('Finally failed to get audio file from bos after retries.')

    except Exception as e:
        tr = traceback.format_exc() + "\naudio:" + file_path + "\nfile_location: bos"
        print(tr)
        logging.error('error happened during process task: %s' % e)

        resp.statusCode = -1
        resp.statusMsg = str(e)

    return resp

