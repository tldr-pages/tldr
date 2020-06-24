#!/usr/bin/env python3

import os
import sys
import json
import urllib.request

BOT_URL = 'https://tldr-bot.starbeamrainbowlabs.com'

COMMENT_ERROR="""
The [build](https://github.com/tldr-pages/tldr/actions/runs/{build_id}) for this PR failed with the following error(s):

```
{content}
```

Please fix the error(s) and push again.
"""

COMMENT_CHECK="""
Hello! I've noticed something unusual when checking this PR:

{content}

Is this intended? If so, just ignore this comment. Otherwise, please double-check the commits.
"""

################################################################################

def post_comment(pr_id, body, once):
  endpoint = BOT_URL + '/comment'

  if once:
    endpoint += '/once'

  headers = {'Content-Type': 'application/json'}
  data = json.dumps({'pr_id': pr_id, 'body': body})
  req = urllib.request.Request(endpoint, data.encode(), headers)

  try:
    resp = urllib.request.urlopen(req)
    code = resp.getcode()
  except Exception as e:
    print('Error sending data to tldr-bot:', str(e), file=sys.stderr)
    return False

  if code != 200:
    print('Error: tldr-bot responded with code', code, file=sys.stderr)
    print(resp.read(), file=sys.stderr)
    return False

  return True

def main(action):
  if action not in ('report-errors', 'report-check-results'):
    print('Unknown action:', action, file=sys.stderr)
    sys.exit(1)

  content = sys.stdin.read().strip()

  if action == 'report-errors':
    comment_body = COMMENT_ERROR.format(build_id=BUILD_ID, content=content)
    comment_once = False
  elif action == 'report-check-results':
    comment_body = COMMENT_CHECK.format(content=content)
    comment_once = True

  if post_comment(PR_ID, comment_body, comment_once):
    print('Success.')
  else:
    print('Error sending data to tldr-bot!', file=sys.stderr)

################################################################################

if __name__ == '__main__':
  REPO_SLUG = os.environ.get('GITHUB_REPOSITORY')
  PR_ID = os.environ.get('PULL_REQUEST_ID')
  BUILD_ID = os.environ.get('GITHUB_RUN_ID')

  if PR_ID is None or BUILD_ID is None or REPO_SLUG is None:
    print('Needed environment variables are not set.', file=sys.stderr)
    sys.exit(1)

  if PR_ID is None or PR_ID == 'false':
    print('Not a pull request, refusing to run.', file=sys.stderr)
    sys.exit(0)

  if len(sys.argv) != 2:
    print('Usage:', sys.argv[0], '<ACTION>', file=sys.stderr)
    sys.exit(1)

  main(sys.argv[1])
