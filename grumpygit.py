import getopt
import sys
from fetchData import getReactions
import json
from github3 import login
import os


def json_pretty(data):
    return json.dumps(data, indent=4, sort_keys=True)


def main(argv):
    org = 'you54f'
    repos = []
    fileName = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["org=", "access="])
    except getopt.GetoptError:
        print('gitmoji.py --org <org>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('gitmoji.py --org <org>')
            sys.exit()
        if opt in ("-o", "--org"):
            org = arg
        if opt in ("-i", "--i"):
            fileName = arg
        if opt in ("-a", "--access"):
            token = id = os.environ.get('GITHUB_TOKEN')
            gh = login(token=token)
            try:
                org_gh = gh.organization(org)
                repos_list = list(org_gh.repositories(type=arg))
            except:
                repos_list = gh.repositories('owner')
            for r in repos_list:
                repos.append(str(r).split("/")[1])
    results = []
    print(gh.octocat(f"Grumpygit - Analysing {org}"))
    if fileName:
        f = open(fileName)
        repos = json.load(f)
        f.close()
    for repo in repos:
        result = getReactions(org, repo)
        if result:
            results.append({repo: result})
    grumpygit_report = json_pretty({
        f"org": org, "overall_sentiment": results})
    print(grumpygit_report)
    f = open(f"results/grumpygit-results-{org}.json", "w")
    f.write(grumpygit_report)
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
