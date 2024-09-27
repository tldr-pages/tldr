#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import os
import sys
import requests

COMMENT_ERROR = """
The [build](https://github.com/tldr-pages/tldr/actions/runs/{build_id}) for this PR failed with the following error(s):

```
{content}
```

Please fix the error(s) and push again.
"""

COMMENT_CHECK = """
Hello! I've noticed something unusual when checking this PR:

{content}

Is this intended? If so, just ignore this comment. Otherwise, please double-check the commits.
"""

################################################################################


# Post a comment to a GitHub issue/pr
def post_comment(issue_id, body):
    url = f"{GITHUB_API_URL}/repos/tldr-pages/tldr/issues/{issue_id}/comments"
    headers = {"Authorization": "token " + BOT_TOKEN}
    data = {"body": body}

    resp = requests.post(url, json=data, headers=headers)
    if resp.status_code != 201:
        print(f"Error posting comment: {resp.text}", file=sys.stderr)
        return False
    return True


# Delete a comment from GitHub
def delete_comment(comment_id):
    url = f"{GITHUB_API_URL}/repos/tldr-pages/tldr/issues/comments/{comment_id}"
    headers = {"Authorization": "token " + BOT_TOKEN}

    resp = requests.delete(url, headers=headers)
    if resp.status_code != 204:
        print(f"Error deleting comment: {resp.text}", file=sys.stderr)
        return False
    return True


# Check for a previous comment by identifier
def previous_comment(issue_id, identifier):
    url = f"{GITHUB_API_URL}/repos/tldr-pages/tldr/issues/{issue_id}/comments"
    headers = {"Authorization": "token " + BOT_TOKEN}
    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        print(f"Error retrieving comments: {resp.text}", file=sys.stderr)
        return None

    comments = resp.json()
    for comment in comments:
        if comment["user"]["login"] == "github-actions" and identifier in comment["body"]:
            return comment["id"]
    return None


################################################################################


# Main function to handle actions
def main(action):
    if action not in ("report-errors", "report-check-results"):
        print(f"Unknown action: {action}", file=sys.stderr)
        sys.exit(1)

    content = sys.stdin.read().strip()

    if action == "report-errors":
        comment_body = COMMENT_ERROR.format(build_id=BUILD_ID, content=content)
    elif action == "report-check-results":
        comment_body = COMMENT_CHECK.format(content=content)

    if "<!-- tldr-bot - errors -->" in comment_body:
        identifier = "<!-- tldr-bot - errors -->"
    elif "<!-- tldr-bot - check-results -->" in comment_body:
        identifier = "<!-- tldr-bot - check-results -->"
    else:
        identifier = None

    if identifier:
        comment_id = previous_comment(PR_ID, identifier)
    else:
        comment_id = None

    if comment_id:
        # Delete previous comment.
        if not delete_comment(comment_id):
            print("Error deleting previous comment!", file=sys.stderr)
            sys.exit(1)

    if post_comment(PR_ID, comment_body):
        print("Success.")
    else:
        print("Error sending data to GitHub!", file=sys.stderr)


################################################################################


# Ensure that the script only runs when executed directly
if __name__ == "__main__":
    # Environment variables required for GitHub API and repo details
    GITHUB_API_URL = "https://api.github.com"
    BOT_TOKEN = os.getenv("GITHUB_TOKEN")
    PR_ID = os.getenv("PULL_REQUEST_ID")
    BUILD_ID = os.getenv("GITHUB_RUN_ID")

    if BOT_TOKEN is None or PR_ID is None or BUILD_ID is None:
        print("Needed environment variables are not set.", file=sys.stderr)
        if BOT_TOKEN is None:
            print("BOT_TOKEN missing...", file=sys.stderr)
        print(f"PR_ID: {PR_ID} and BUILD_ID: {BUILD_ID}")
        sys.exit(1)

    if PR_ID is None or PR_ID == "false":
        print("Not a pull request, refusing to run.", file=sys.stderr)
        sys.exit(0)

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <ACTION>", file=sys.stderr)
        sys.exit(1)

    main(sys.argv[1])
