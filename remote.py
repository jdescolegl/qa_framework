import os
import requests
import json
from pathlib import Path, PurePosixPath

# El número de threads que se corren en paralelo debe coincidir con la cantidad
# de nodos/carpetas presentes en la fixture pytest_xdist_make_scheduler del archivo
# conftest.py

def trigger_github_actions_regression(current_pytest_args):
    GITHUB_ACTIONS_QA_REPO_ENDPOINT = 'https://api.github.com/'
    env = os.environ["env"]
    country = os.environ["country"]
    event_type = 'parametrized-{country}-regression-event'.format(country=country)
    branch = get_current_branch()
    github_token = get_github_token()

    if current_pytest_args.keyword:
        github_post_args = '-k {}'.format(current_pytest_args.keyword)

    else:
        github_post_args = '-m {}'.format(current_pytest_args.markexpr)

    payload = {'event_type': event_type,
               'client_payload': {
                   'branch': branch,
                   'profile': env,
                   'country': country,
                   'args': github_post_args
                    }
               }

    headers = {'Accept': 'application/vnd.github.everest-preview+json',
               'Authorization': 'token {}'.format(github_token),
               'Content-Type': 'application/json'}

    response = requests.post(url=GITHUB_ACTIONS_QA_REPO_ENDPOINT, data=json.dumps(payload), headers=headers)
    print('POST Status Code: {}'.format(response.status_code))


def get_current_branch():
    with open('.git/HEAD', 'r', newline='') as file:
        data = file.readline()
        branch = data.split('/')[2][:-1]
        return branch


def get_github_token():
    while True:
        try:
            github_token = read_github_token_from_file()
            return github_token
        except FileNotFoundError:
            ght = input("GitHub Token not found. Please enter a valid token: ")
            save_github_token(ght)

def read_github_token_from_file():
    user_home_path = Path.home()
    github_token_filename = '.ght'
    github_token_filepath = PurePosixPath.joinpath(user_home_path).joinpath(github_token_filename)
    with open(github_token_filepath) as file:
        data = file.readline()
        return data

def save_github_token(ght):
    user_home_path = Path.home()
    github_token_filename = '.ght'
    github_token_filepath = PurePosixPath.joinpath(user_home_path).joinpath(github_token_filename)
    with open(github_token_filepath, 'w') as file:
        file.write(ght)

