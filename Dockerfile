FROM ubuntu:18.04
MAINTAINER lilf <lf97310@gmail.com>

ENV TZ=Asia/Shanghai

RUN apt-get update -y && \
    apt-get install -y python3.6 python3-pip python3.6-dev

# 并更新pip
RUN python3.6 -m pip install pip --upgrade -i https://pypi.douban.com/simple && \
    python3.6 -m pip install wheel -i https://pypi.douban.com/simple

# 设置pip源
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple/ && \
    pip3 config set global.trusted-host mirrors.aliyun.com

RUN pip3 install --no-cache-dir thrift thriftpy2 && \
    pip3 install --no-cache-dir mongoengine requests numpy pycrypto && \
    pip3 install --no-cache-dir webrtcvad pypinyin zhon python-Levenshtein

EXPOSE 9093

WORKDIR /expression-analysis
COPY ./ /expression-analysis

ENTRYPOINT ["python3.6", "server.py"]