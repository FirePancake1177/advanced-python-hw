FROM python:3.13-slim-bookworm

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-lang-cyrillic \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-extra-utils \
    latexmk \
    wget && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /app

COPY example_usage_lib/pyproject.toml example_usage_lib/poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY example_usage_lib/src/example_usage_lib ./src/example_usage_lib

RUN mkdir -p /app/artifacts

CMD ["sh", "-c", "cd src/example_usage_lib && \
    python generate_latex.py && \
    pdflatex -interaction=nonstopmode -output-directory /app/artifacts example_full.tex"]