import json
import logging
import time
import traceback

import jwt

import analysis_features
from analysis.ttypes import *
import service
from errors import *
from utils_file import get_wav_file_bytes_io


def analyze_reading_question(request: AnalyzeReadingQuestionRequest) -> AnalyzeReadingQuestionResponse:
    resp = AnalyzeReadingQuestionResponse()

    file_path = request.filePath
    std_text = request.stdText
    result = {}

    if file_path == "" or file_path is None:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        file = get_wav_file_bytes_io(file_path, "bos")
        if file is not None:
            result = analysis_features.analysis1(file, std_text)
        else:
            logging.error('pre-test: Finally failed to get audio file from bos after retries.')

        resp.result = json.dumps(result)
        fill_status_of_resp(resp)
    except Exception as e:
        tr = traceback.format_exc() + "\naudio:" + file_path + "\nfile_location: bos"
        print(tr)
        logging.error('error happened during process task: %s' % e)

        resp.statusCode = -1
        resp.statusMsg = "error happened during process task"

    return resp


def analyze_retelling_question(self, request: AnalyzeRetellingQuestionRequest) -> AnalyzeRetellingQuestionResponse:
    pass


def analyze_expression_question(self, request: AnalyzeExpressionQuestionRequest) -> AnalyzeExpressionQuestionResponse:
    pass
