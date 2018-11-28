FROM Python:3

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN pip3 install \
    flask \
    numpy \
    pillow

WORKDIR /workspace
RUN chmod -R a+w /workspace
COPY svm.pkl /workspace
COPY main.py /workspace
RUN chmod +x /workspace/main.py
CMD python3 /workspace/main.py

EXPOSE 5000
