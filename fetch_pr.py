from datetime import datetime
import pandas as pd
import requests
import json
import logging
from tabulate import tabulate


"""
static vars go here 
"""
_PR_DETAILS_LIST = list()
_REPO_OWNER = 'vinodgowda1477'
_REPO = 'github_pr'
_LIST_PR_URL = f"https://api.github.com/repos/{_REPO_OWNER}/{_REPO}/pulls?state=all"

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
            _PR_DICT["assignee"] =  value["assignee"]
            _PR_DETAILS_LIST.append(_PR_DICT)

"""
This method prints PR details in readable table format
"""
def format_data():
    df_data = pd.DataFrame.from_records([s for s in _PR_DETAILS_LIST])
    headers = ['PR Id', 'PR Title', 'Source', 'Target', 'Status', 'Created on', 'Updated on', 'Closed on', 'PR raised by', 'Assignee']
    print(tabulate(df_data, headers= headers, showindex=False, tablefmt='psql'))


fetch_pr_details()
format_data()
# print(_PR_DETAILS_LIST)
    # dfi = pd.read_json(url)
    # if dfi.empty:
    #     break
    # dfs.append(dfi)  # add dataframe to list of dataframes
    # page += 1  # Advance onto the next page

# df = pd.concat(dfs, axis='rows', ignore_index=True)

# Create a new column with usernames
# df['username'] = pd.json_normalize(df['user'])['login']