# grumpygit

GitHub gave us [emojis](https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/)

But they didn't give [notifications](https://github.com/github/feedback/discussions/5911) to feed our 🧠

> Our brain loves social media notifications. Whenever we see a notification from our social media sites, either from Facebook, Instagram or Twitter, our brain releases a small amount of dopamine. Dopamine is a chemical produced by the brain when we feel rewarded or pleasure

I often wonder if GitHub Issues are full of grumpy gits, or happy campers.

- For emojis! 👍 👎 😄 😕 ❤️ 🎉
- Check across a GitHub Organisation
- Check across specific Repos

Find every issue in your GitHub Organisation or repositories, which has had an emoji reaction, included nested in comments.

- handles the edge case where there are more than 100 emojis under a comment.
- handles the limitation of Github API where you have a quota on the number of requests per hour. The program will sleep when it almost hits the limit and it will retry after 1 minute.

## How to run

Get your own [token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) from Github and add it as an env var `GITHUB_TOKEN`

## Usage via Github Fork

- Fork the repo
- update `./grumpygit` with your `username` or `org` in the matrix section
- add an `ORG_TOKEN` secret, as per above steps.
- add a `REPO_TOKEN` with write access if you want to write the file back to the repo

## Usage via Github Actions

> Note, this is untested at the moment

- `GITHUB_TOKEN` _Required_ Set as an env var
- `ORG_NAME` _Required_
- One of the following
  - `REPO_LIST` _optional_
    - `json` file containing an array of repo names
  - `ACCESS` _optional_
    - `public` or `all`
    - (token must have private read rights if selecting all)

File will be committed back to the repository, in results folder.

`results/grumpygit-results-${ORG_NAME}.json`

## Usage Directly

- `python grumpygit.py --org <org_name> -f <list_of_repos.json>`
- `python grumpygit.py --org <org_name> -a public`
- `python grumpygit.py --org <org_name> -a all`
- `python grumpygit.py --org <username>`

### Pre-reqs

- Python 3.7
  - `requests`
  - `github3`

### Pipenv

```bash
pipenv install
```

#### shell

```bash
pipenv shell
python run grumpy-git.py
```

#### pipenv run

```bash
pipenv run python grumpy-git.py
```

### pip

```bash
pip install -r requirements.txt
```

#### python

```bash
python run grumpy-git.py
```

## Credits

- Initially based on [ansonyao](https://github.com/ansonyao)'s [githubEmojiReactions](https://github.com/ansonyao/githubEmojiReactions) program.
