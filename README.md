<!-- GETTING STARTED -->
## Introduction

This is simple python script which gives the list of PR's associated with any public repository by taking repo owner and repo name as an input.

### Prerequisites

1. Make sure docker is installed to build image and run the container

<!-- USAGE EXAMPLES -->
## Usage

* Build docker image when email functionality is disabled (Preferred usage)
  ```
  docker build -t <image_name>:<image_tag> --build-arg _REPO_OWNER=<repo owner or organisation> \
  --build-arg _REPO_NAME=<repo name> --no-cache .

  sample cmd:
  docker build -t fetch_pr:v1 --build-arg _REPO_OWNER="vinodgowda1477" --build-arg _REPO_NAME="github_pr" --no-cache .
  ```
  
* Run the docker container using the image built in above step
  ```
  docker run -it <image_name>:<image_tag> 
  
  sample cmd:
  docker run -it fetch_pr:v1 
  ```


##
Note: Commenting out email related code block
####
In case 2 factor authentication is enabled for your gmail, 16 digit account password needed to be generated and passed as a value to build 
argument _MAIL_PASSWD while building image. Normal console password won't work and will throw exception while running the method email_pr_details()
Reference: https://support.google.com/accounts/answer/185833?visit_id=638228703261679041-1014494481&p=InvalidSecondFactor&rd=1



* Build docker image when email functionality is enabled.(In case 16 digit account password is generated referencing above link)
  ```
  docker build -t <image_name>:<image_tag> --build-arg _REPO_OWNER=<repo owner or organisation> \
  --build-arg _REPO_NAME=<repo name> --build-arg _SENDER_MAIL=<sender mail> \ 
  --build-arg _RECEIVER_MAIL=<receiver mail> --build-arg _MAIL_PASSWD=<16 digit auth token> --no-cache .

  sample cmd:
  docker build -t fetch_pr:v1 --build-arg _REPO_OWNER="vinodgowda1477" --build-arg _REPO_NAME="github_pr" --build-arg \
  _SENDER_MAIL="sender@gmail.com" --build-arg _RECEIVER_MAIL=receiver@gmail.com \
  --build-arg _MAIL_PASSWD="Your acoount token" --no-cache .
  ```