FROM python:3

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN pip3 install \
    flask \
    numpy \
    scipy \
    sklearn \
    pillow

RUN mkdir /usr/src/resnet
WORKDIR /workspace
RUN chmod -R a+w /workspace
COPY svm.model /workspace
COPY main.py /workspace
RUN chmod +x /workspace/main.py
CMD python3 /workspace/main.py

EXPOSE 5000