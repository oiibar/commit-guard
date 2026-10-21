import sys
import requests

API="https://api.github.com"

def fetch_commit(owner,repo,sha):
    url=f"{API}/repos/{owner}/{repo}/commits/{sha}"
    response=requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    if len(sys.argv)!=4:
        print("Usage: python fetch_diff.py <owner> <repo> <sha>")
        print("Example: python fetch_diff.py oiibar commit-guard 610db04")
        sys.exit(1)


    owner,repo,sha=sys.argv[1],sys.argv[2],sys.argv[3]
    data=fetch_commit(owner,repo,sha)
    print("Message:",data["commit"]["message"])
    for f in data["files"]:
        print(f["filename"],f["status"])
        print(f.get("patch", "(no patch: binary or too large file)"))
        print()

if __name__ == "__main__":
    main()