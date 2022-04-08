FROM python:3.9.10-slim-buster

WORKDIR /app

# コンソールのstdout（標準出力）とstderr（標準エラー出力）のバッファーを無効
ENV PYTHONUNBUFFERED=1
# pycファイルの生成を無効化
ENV PYTHONDONTWRITEBYTECODE=1

# 各種パッケージインストール
RUN apt-get update && \
    apt-get install -y curl git zsh ca-certificates vim postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# poetryのインストール＆pythonパッケージインストール
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY app/pyproject.toml app/poetry.lock ./

RUN if [ -f pyproject.toml ]; then poetry install; fi

COPY app/ ./
