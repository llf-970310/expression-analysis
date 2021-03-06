#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class AnalyzeReadingQuestionRequest(object):
    """
    Attributes:
     - filePath
     - stdText

    """


    def __init__(self, filePath=None, stdText=None,):
        self.filePath = filePath
        self.stdText = stdText

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.filePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.stdText = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AnalyzeReadingQuestionRequest')
        if self.filePath is not None:
            oprot.writeFieldBegin('filePath', TType.STRING, 1)
            oprot.writeString(self.filePath.encode('utf-8') if sys.version_info[0] == 2 else self.filePath)
            oprot.writeFieldEnd()
        if self.stdText is not None:
            oprot.writeFieldBegin('stdText', TType.STRING, 2)
            oprot.writeString(self.stdText.encode('utf-8') if sys.version_info[0] == 2 else self.stdText)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.filePath is None:
            raise TProtocolException(message='Required field filePath is unset!')
        if self.stdText is None:
            raise TProtocolException(message='Required field stdText is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AnalyzeReadingQuestionResponse(object):
    """
    Attributes:
     - feature
     - qualityScore
     - statusCode
     - statusMsg

    """


    def __init__(self, feature=None, qualityScore=None, statusCode=None, statusMsg=None,):
        self.feature = feature
        self.qualityScore = qualityScore
        self.statusCode = statusCode
        self.statusMsg = statusMsg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.feature = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.qualityScore = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.statusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.statusMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AnalyzeReadingQuestionResponse')
        if self.feature is not None:
            oprot.writeFieldBegin('feature', TType.STRING, 1)
            oprot.writeString(self.feature.encode('utf-8') if sys.version_info[0] == 2 else self.feature)
            oprot.writeFieldEnd()
        if self.qualityScore is not None:
            oprot.writeFieldBegin('qualityScore', TType.DOUBLE, 2)
            oprot.writeDouble(self.qualityScore)
            oprot.writeFieldEnd()
        if self.statusCode is not None:
            oprot.writeFieldBegin('statusCode', TType.I32, 3)
            oprot.writeI32(self.statusCode)
            oprot.writeFieldEnd()
        if self.statusMsg is not None:
            oprot.writeFieldBegin('statusMsg', TType.STRING, 4)
            oprot.writeString(self.statusMsg.encode('utf-8') if sys.version_info[0] == 2 else self.statusMsg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.feature is None:
            raise TProtocolException(message='Required field feature is unset!')
        if self.qualityScore is None:
            raise TProtocolException(message='Required field qualityScore is unset!')
        if self.statusCode is None:
            raise TProtocolException(message='Required field statusCode is unset!')
        if self.statusMsg is None:
            raise TProtocolException(message='Required field statusMsg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AnalyzeRetellingQuestionRequest(object):
    """
    Attributes:
     - filePath
     - voiceFeatures
     - keywords
     - detailwords
     - keyWeights
     - detailWeights

    """


    def __init__(self, filePath=None, voiceFeatures=None, keywords=None, detailwords=None, keyWeights=None, detailWeights=None,):
        self.filePath = filePath
        self.voiceFeatures = voiceFeatures
        self.keywords = keywords
        self.detailwords = detailwords
        self.keyWeights = keyWeights
        self.detailWeights = detailWeights

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.filePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.voiceFeatures = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.keywords = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = []
                        (_etype9, _size6) = iprot.readListBegin()
                        for _i10 in range(_size6):
                            _elem11 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                            _elem5.append(_elem11)
                        iprot.readListEnd()
                        self.keywords.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.detailwords = []
                    (_etype15, _size12) = iprot.readListBegin()
                    for _i16 in range(_size12):
                        _elem17 = []
                        (_etype21, _size18) = iprot.readListBegin()
                        for _i22 in range(_size18):
                            _elem23 = []
                            (_etype27, _size24) = iprot.readListBegin()
                            for _i28 in range(_size24):
                                _elem29 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                                _elem23.append(_elem29)
                            iprot.readListEnd()
                            _elem17.append(_elem23)
                        iprot.readListEnd()
                        self.detailwords.append(_elem17)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.keyWeights = []
                    (_etype33, _size30) = iprot.readListBegin()
                    for _i34 in range(_size30):
                        _elem35 = iprot.readDouble()
                        self.keyWeights.append(_elem35)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.detailWeights = []
                    (_etype39, _size36) = iprot.readListBegin()
                    for _i40 in range(_size36):
                        _elem41 = iprot.readDouble()
                        self.detailWeights.append(_elem41)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AnalyzeRetellingQuestionRequest')
        if self.filePath is not None:
            oprot.writeFieldBegin('filePath', TType.STRING, 1)
            oprot.writeString(self.filePath.encode('utf-8') if sys.version_info[0] == 2 else self.filePath)
            oprot.writeFieldEnd()
        if self.voiceFeatures is not None:
            oprot.writeFieldBegin('voiceFeatures', TType.STRING, 2)
            oprot.writeString(self.voiceFeatures.encode('utf-8') if sys.version_info[0] == 2 else self.voiceFeatures)
            oprot.writeFieldEnd()
        if self.keywords is not None:
            oprot.writeFieldBegin('keywords', TType.LIST, 3)
            oprot.writeListBegin(TType.LIST, len(self.keywords))
            for iter42 in self.keywords:
                oprot.writeListBegin(TType.STRING, len(iter42))
                for iter43 in iter42:
                    oprot.writeString(iter43.encode('utf-8') if sys.version_info[0] == 2 else iter43)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.detailwords is not None:
            oprot.writeFieldBegin('detailwords', TType.LIST, 4)
            oprot.writeListBegin(TType.LIST, len(self.detailwords))
            for iter44 in self.detailwords:
                oprot.writeListBegin(TType.LIST, len(iter44))
                for iter45 in iter44:
                    oprot.writeListBegin(TType.STRING, len(iter45))
                    for iter46 in iter45:
                        oprot.writeString(iter46.encode('utf-8') if sys.version_info[0] == 2 else iter46)
                    oprot.writeListEnd()
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.keyWeights is not None:
            oprot.writeFieldBegin('keyWeights', TType.LIST, 5)
            oprot.writeListBegin(TType.DOUBLE, len(self.keyWeights))
            for iter47 in self.keyWeights:
                oprot.writeDouble(iter47)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.detailWeights is not None:
            oprot.writeFieldBegin('detailWeights', TType.LIST, 6)
            oprot.writeListBegin(TType.DOUBLE, len(self.detailWeights))
            for iter48 in self.detailWeights:
                oprot.writeDouble(iter48)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.keywords is None:
            raise TProtocolException(message='Required field keywords is unset!')
        if self.detailwords is None:
            raise TProtocolException(message='Required field detailwords is unset!')
        if self.keyWeights is None:
            raise TProtocolException(message='Required field keyWeights is unset!')
        if self.detailWeights is None:
            raise TProtocolException(message='Required field detailWeights is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AnalyzeRetellingQuestionResponse(object):
    """
    Attributes:
     - feature
     - keyScore
     - detailScore
     - statusCode
     - statusMsg

    """


    def __init__(self, feature=None, keyScore=None, detailScore=None, statusCode=None, statusMsg=None,):
        self.feature = feature
        self.keyScore = keyScore
        self.detailScore = detailScore
        self.statusCode = statusCode
        self.statusMsg = statusMsg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.feature = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.keyScore = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.DOUBLE:
                    self.detailScore = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.statusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.statusMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AnalyzeRetellingQuestionResponse')
        if self.feature is not None:
            oprot.writeFieldBegin('feature', TType.STRING, 1)
            oprot.writeString(self.feature.encode('utf-8') if sys.version_info[0] == 2 else self.feature)
            oprot.writeFieldEnd()
        if self.keyScore is not None:
            oprot.writeFieldBegin('keyScore', TType.DOUBLE, 2)
            oprot.writeDouble(self.keyScore)
            oprot.writeFieldEnd()
        if self.detailScore is not None:
            oprot.writeFieldBegin('detailScore', TType.DOUBLE, 3)
            oprot.writeDouble(self.detailScore)
            oprot.writeFieldEnd()
        if self.statusCode is not None:
            oprot.writeFieldBegin('statusCode', TType.I32, 4)
            oprot.writeI32(self.statusCode)
            oprot.writeFieldEnd()
        if self.statusMsg is not None:
            oprot.writeFieldBegin('statusMsg', TType.STRING, 5)
            oprot.writeString(self.statusMsg.encode('utf-8') if sys.version_info[0] == 2 else self.statusMsg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.feature is None:
            raise TProtocolException(message='Required field feature is unset!')
        if self.keyScore is None:
            raise TProtocolException(message='Required field keyScore is unset!')
        if self.detailScore is None:
            raise TProtocolException(message='Required field detailScore is unset!')
        if self.statusCode is None:
            raise TProtocolException(message='Required field statusCode is unset!')
        if self.statusMsg is None:
            raise TProtocolException(message='Required field statusMsg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AnalyzeExpressionQuestionRequest(object):
    """
    Attributes:
     - filePath
     - wordbase

    """


    def __init__(self, filePath=None, wordbase=None,):
        self.filePath = filePath
        self.wordbase = wordbase

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.filePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.wordbase = {}
                    (_ktype50, _vtype51, _size49) = iprot.readMapBegin()
                    for _i53 in range(_size49):
                        _key54 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val55 = []
                        (_etype59, _size56) = iprot.readListBegin()
                        for _i60 in range(_size56):
                            _elem61 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                            _val55.append(_elem61)
                        iprot.readListEnd()
                        self.wordbase[_key54] = _val55
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AnalyzeExpressionQuestionRequest')
        if self.filePath is not None:
            oprot.writeFieldBegin('filePath', TType.STRING, 1)
            oprot.writeString(self.filePath.encode('utf-8') if sys.version_info[0] == 2 else self.filePath)
            oprot.writeFieldEnd()
        if self.wordbase is not None:
            oprot.writeFieldBegin('wordbase', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.LIST, len(self.wordbase))
            for kiter62, viter63 in self.wordbase.items():
                oprot.writeString(kiter62.encode('utf-8') if sys.version_info[0] == 2 else kiter62)
                oprot.writeListBegin(TType.STRING, len(viter63))
                for iter64 in viter63:
                    oprot.writeString(iter64.encode('utf-8') if sys.version_info[0] == 2 else iter64)
                oprot.writeListEnd()
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.filePath is None:
            raise TProtocolException(message='Required field filePath is unset!')
        if self.wordbase is None:
            raise TProtocolException(message='Required field wordbase is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AnalyzeExpressionQuestionResponse(object):
    """
    Attributes:
     - feature
     - structureScore
     - logicScore
     - statusCode
     - statusMsg

    """


    def __init__(self, feature=None, structureScore=None, logicScore=None, statusCode=None, statusMsg=None,):
        self.feature = feature
        self.structureScore = structureScore
        self.logicScore = logicScore
        self.statusCode = statusCode
        self.statusMsg = statusMsg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.feature = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.structureScore = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.DOUBLE:
                    self.logicScore = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.statusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.statusMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AnalyzeExpressionQuestionResponse')
        if self.feature is not None:
            oprot.writeFieldBegin('feature', TType.STRING, 1)
            oprot.writeString(self.feature.encode('utf-8') if sys.version_info[0] == 2 else self.feature)
            oprot.writeFieldEnd()
        if self.structureScore is not None:
            oprot.writeFieldBegin('structureScore', TType.DOUBLE, 2)
            oprot.writeDouble(self.structureScore)
            oprot.writeFieldEnd()
        if self.logicScore is not None:
            oprot.writeFieldBegin('logicScore', TType.DOUBLE, 3)
            oprot.writeDouble(self.logicScore)
            oprot.writeFieldEnd()
        if self.statusCode is not None:
            oprot.writeFieldBegin('statusCode', TType.I32, 4)
            oprot.writeI32(self.statusCode)
            oprot.writeFieldEnd()
        if self.statusMsg is not None:
            oprot.writeFieldBegin('statusMsg', TType.STRING, 5)
            oprot.writeString(self.statusMsg.encode('utf-8') if sys.version_info[0] == 2 else self.statusMsg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.feature is None:
            raise TProtocolException(message='Required field feature is unset!')
        if self.structureScore is None:
            raise TProtocolException(message='Required field structureScore is unset!')
        if self.logicScore is None:
            raise TProtocolException(message='Required field logicScore is unset!')
        if self.statusCode is None:
            raise TProtocolException(message='Required field statusCode is unset!')
        if self.statusMsg is None:
            raise TProtocolException(message='Required field statusMsg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(AnalyzeReadingQuestionRequest)
AnalyzeReadingQuestionRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'filePath', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'stdText', 'UTF8', None, ),  # 2
)
all_structs.append(AnalyzeReadingQuestionResponse)
AnalyzeReadingQuestionResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'feature', 'UTF8', None, ),  # 1
    (2, TType.DOUBLE, 'qualityScore', None, None, ),  # 2
    (3, TType.I32, 'statusCode', None, None, ),  # 3
    (4, TType.STRING, 'statusMsg', 'UTF8', None, ),  # 4
)
all_structs.append(AnalyzeRetellingQuestionRequest)
AnalyzeRetellingQuestionRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'filePath', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'voiceFeatures', 'UTF8', None, ),  # 2
    (3, TType.LIST, 'keywords', (TType.LIST, (TType.STRING, 'UTF8', False), False), None, ),  # 3
    (4, TType.LIST, 'detailwords', (TType.LIST, (TType.LIST, (TType.STRING, 'UTF8', False), False), False), None, ),  # 4
    (5, TType.LIST, 'keyWeights', (TType.DOUBLE, None, False), None, ),  # 5
    (6, TType.LIST, 'detailWeights', (TType.DOUBLE, None, False), None, ),  # 6
)
all_structs.append(AnalyzeRetellingQuestionResponse)
AnalyzeRetellingQuestionResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'feature', 'UTF8', None, ),  # 1
    (2, TType.DOUBLE, 'keyScore', None, None, ),  # 2
    (3, TType.DOUBLE, 'detailScore', None, None, ),  # 3
    (4, TType.I32, 'statusCode', None, None, ),  # 4
    (5, TType.STRING, 'statusMsg', 'UTF8', None, ),  # 5
)
all_structs.append(AnalyzeExpressionQuestionRequest)
AnalyzeExpressionQuestionRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'filePath', 'UTF8', None, ),  # 1
    (2, TType.MAP, 'wordbase', (TType.STRING, 'UTF8', TType.LIST, (TType.STRING, 'UTF8', False), False), None, ),  # 2
)
all_structs.append(AnalyzeExpressionQuestionResponse)
AnalyzeExpressionQuestionResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'feature', 'UTF8', None, ),  # 1
    (2, TType.DOUBLE, 'structureScore', None, None, ),  # 2
    (3, TType.DOUBLE, 'logicScore', None, None, ),  # 3
    (4, TType.I32, 'statusCode', None, None, ),  # 4
    (5, TType.STRING, 'statusMsg', 'UTF8', None, ),  # 5
)
fix_spec(all_structs)
del all_structs
