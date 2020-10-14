import os
import sys

project_folder = os.path.abspath(__file__).split('/server.py')[0]
sys.path.append(os.path.join(project_folder, 'expression'))
sys.path.append(os.path.join(project_folder, 'gen-py'))

import logging

import mongoengine
from config import MongoConfig
from analysis import AnalysisService
from analysis.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import handler


class AnalysisServiceHandler:
    def __init__(self):
        self.log = {}

    def analyzeReadingQuestion(self, request: AnalyzeReadingQuestionRequest) -> AnalyzeReadingQuestionResponse:
        return handler.analyze_reading_question(request)

    def analyzeRetellingQuestion(self, request: AnalyzeRetellingQuestionRequest) -> AnalyzeRetellingQuestionResponse:
        return handler.analyze_retelling_question(request)

    def analyzeExpressionQuestion(self, request: AnalyzeExpressionQuestionRequest) -> AnalyzeExpressionQuestionResponse:
        return handler.analyze_expression_question(request)

    def analyzeSentence(self, request: AnalyzeSentenceRequest) -> AnalyzeSentenceResponse:
        return handler.analyze_sentence(request)


if __name__ == '__main__':
    # init mongo
    mongoengine.connect(
        db=MongoConfig.db,
        host=MongoConfig.host,
        port=MongoConfig.port,
        username=MongoConfig.user,
        password=MongoConfig.password
    )

    # init logging
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

    # init thrift server
    exam_handler = AnalysisServiceHandler()
    processor = AnalysisService.Processor(exam_handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9093)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    # You could do one of these for a multithreaded server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    server.serve()
