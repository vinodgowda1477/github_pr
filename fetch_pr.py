from datetime import datetime
import pandas as pd
import requests
import json
import sys
from tabulate import tabulate
import smtplib
from email.mime.text import MIMEText


# """
# System arguments
# """
# repo_owner = sys.argv[1]
# repo_name = sys.argv[2]
# sender_email = sys.argv[3]
# receiver_email = sys.argv[4]
# gmail_password = sys.argv[5]

"""
static vars go here 
"""
_PR_DETAILS_LIST = list()
_REPO_OWNER = sys.argv[1]
_REPO = sys.argv[2]
_LIST_PR_URL = f"https://api.github.com/repos/{_REPO_OWNER}/{_REPO}/pulls?state=all"

### MAIL DETAILS
_SUBJECT = "List of PR: Repo: %s" % _REPO
_SENDER = "test@gmail.com"
_RECIPIENTS = ["test2@gmail.com"]
_PASSWORD = "test@test"


"""
This method filters out PR's which are older than 1 week
"""
def filter_latest_pr(pr_creation_date):
    pr_date = datetime.strftime(datetime.strptime(pr_creation_date, '%Y-%m-%dT%H:%M:%S%z'), "%Y-%m-%d")
    now = datetime.now()
    return (now - datetime.strptime(pr_date, '%Y-%m-%d')).days < 7


"""
This method fetches list of pr for given repo
and filters out required fields
"""
def fetch_pr_details():
    response = requests.get(url=_LIST_PR_URL)
    pr_response_list = json.loads(response.content)
    for value in pr_response_list:
        _PR_DICT = dict()
        if filter_latest_pr(value["created_at"]):
            _PR_DICT["pr_id"] = value["number"]
            _PR_DICT["pr_title"] = value["title"]
            _PR_DICT["source_branch"] = value["head"]["ref"]
            _PR_DICT["target_branch"] = value["base"]["ref"]
            _PR_DICT["pr_status"] = value["state"]
            _PR_DICT["created_on"] = value["created_at"]
            _PR_DICT["updated_on"] = value["updated_at"]
            _PR_DICT["closed_on"] = value["closed_at"]
            _PR_DICT["pr_raised_by"] = value["head"]["user"]["login"]
            _PR_DICT["assignee"] =  value.get('assignee').get('login') if value.get("assignee") else 'NA'
            _PR_DICT["reviewers"] =  value["requested_reviewers"]
            _PR_DETAILS_LIST.append(_PR_DICT)

"""
This method sends the email of PR details in required format
"""
def email_pr_details(df_data):
    msg = MIMEText(df_data)
    msg['Subject'] = _SUBJECT
    msg['From'] = _SENDER
    msg['To'] = ', '.join(_RECIPIENTS)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(_SENDER, _PASSWORD)
        smtp_server.sendmail(_SENDER, _RECIPIENTS, msg.as_string())
    print("Email sent successfully")


"""
This method prints PR details in readable table format
"""
def format_data():
    df_data = pd.DataFrame.from_records([s for s in _PR_DETAILS_LIST])
    headers = ['PR Id', 'PR Title', 'Source', 'Target', 'Status', 'Created on', 'Updated on', 'Closed on',
               'PR raised by', 'Assignee', 'Reviewers']
    print("Number of PR's raised: %s" % len(_PR_DETAILS_LIST))
    print(tabulate(df_data, headers= headers, showindex=False, tablefmt='psql'))
    # email_pr_details(df_data.to_html(index=False))


fetch_pr_details()
format_data()

