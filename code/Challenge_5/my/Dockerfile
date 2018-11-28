FROM python:3

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install -U scikit-learn

RUN pip install \
    flask \
    matplotlib \
    pandas \
    numpy \
    scipy \
    pillow

WORKDIR /workspace
RUN chmod -R a+w /workspace
COPY svm.model /workspace
COPY main.py /workspace
RUN chmod +x /workspace/main.py
CMD python /workspace/main.py

EXPOSE 5000
