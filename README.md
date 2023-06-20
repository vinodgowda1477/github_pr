<!-- GETTING STARTED -->
## Introduction

This is simple python script which gives the list of PR's associated with any public repository by taking repo owner and repo name as an input.

### Prerequisites

1. Make sure docker is installed to build image and run the container

<!-- USAGE EXAMPLES -->
## Usage
* Build docker image by passing Repository name and Repository owner as build-args
  ```
  docker build -t <image_name>:<image_tag> --build-arg _REPO_OWNER=<repo owner or organisation> --build-arg _REPO_NAME=<repo name> --no-cache .
  
  sample cmd:
  docker build -t fetch_pr:v1 --build-arg _REPO_OWNER="vinodgowda1477" --build-arg _REPO_NAME="github_pr" --no-cache .
  ```
* Run the docker container using the image built in above step
  ```
  docker run -d --name <container_name> <image_name>:<image_tag> 
  
  sample cmd:
  docker run -d --name github_pr_container fetch_pr:v1 
  ```

