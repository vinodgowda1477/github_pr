FROM python:3.8-alpine
LABEL Maintainer="Vinod R"

ARG _REPO_OWNER="vinodgowda1477"
ARG _REPO_NAME="github_pr"

COPY fetch_pr.py /app/
COPY requirements.txt /app/

WORKDIR /app/
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python", "/app/fetch_pr.py", "${_REPO_OWNER}", "${_REPO_NAME}"]