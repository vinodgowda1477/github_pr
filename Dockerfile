FROM python:3.9-slim
LABEL Maintainer="Vinod R"

ARG _REPO_OWNER="vinodgowda1477"
ARG _REPO_NAME="github_pr"
# ARG _SENDER_MAIL="vinodgowda417@gmail.com"
# ARG _RECEIVER_MAIL="vinodgowda1477@gmail.com"
# ARG _MAIL_PASSWD=""

ENV REPO_OWNER=$_REPO_OWNER
ENV REPO_NAME=$_REPO_NAME
# ENV SENDER_MAIL=$_SENDER_MAIL
# ENV RECEIVER_MAIL=$_RECEIVER_MAIL
# ENV MAIL_PASSWD=$_MAIL_PASSWD
ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD . /app/
RUN pip install -r /app/requirements.txt

ENTRYPOINT python /app/fetch_pr.py $REPO_OWNER $REPO_NAME
# ENTRYPOINT python /app/fetch_pr.py $REPO_OWNER $REPO_NAME $SENDER_MAIL $RECEIVER_MAIL $MAIL_PASSWD
