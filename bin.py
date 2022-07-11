import json, os, requests

headers = {'Authorization': f'token  {os.getenv("GITHUB_TOKEN")}', 'Accept': 'application/vnd.github.v3+json', 'Content-Type': 'application/json'}

if os.getenv("GITHUB_WORKFLOW") == "one":
    data = {"event_type":"second"}
else:
    data = {"event_type":"first"}

url = f'https://api.github.com/repos/{os.getenv("GITHUB_REPOSITORY")}/dispatches'

req = requests.post(url, data=json.dumps(data), headers=headers)

print(req.status_code)
