import pandas as pd
import requests

organization = 'vinodgowda1477'
repository = 'github_pr'
state = 'all'  # other options include 'closed' or 'open'
page = 1  # initialize page number to 1 (first page)
dfs = []  # create empty list to hold individual dataframes
# Note it is necessary to loop as each request retrieves maximum 30 entries
url = f"https://api.github.com/repos/{organization}/{repository}/pulls?state={state}&page={page}"
headers = {"Accept": "application/vnd.github+json",
           "Authorization": "Bearer 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",
           "X-GitHub-Api-Version": "2022-11-28"
}

res = requests.get(url=url, headers=headers)
print(res.content)
    # dfi = pd.read_json(url)
    # if dfi.empty:
    #     break
    # dfs.append(dfi)  # add dataframe to list of dataframes
    # page += 1  # Advance onto the next page

# df = pd.concat(dfs, axis='rows', ignore_index=True)

# Create a new column with usernames
# df['username'] = pd.json_normalize(df['user'])['login']