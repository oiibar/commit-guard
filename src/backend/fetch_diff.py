import sys
import requests

API="https://api.github.com"

def fetch_commit(owner,repo,sha):
    url=f"{API}/repos/{owner}/{repo}/commits/{sha}"
    response=requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()




def main():
    owner,repo,sha=sys.argv[1],sys.argv[2],sys.argv[3]
    data=fetch_commit(owner,repo,sha)
    print("Message:",data["commit"]["message"])
    for f in data["files"]:
        print(f["filename"],f["status"])

if __name__ == "__main__":
    main()