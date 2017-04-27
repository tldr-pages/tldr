import json
import os
import sys
import urllib2

URL = 'https://tldr-bot.starbeamrainbowlabs.com/'

def post_comment(pr_id, comment_body):
  # Constructing the url
  req = urllib2.Request(URL,
                       json.dumps({'body': comment_body, 'pr_id': pr_id }),
                       {'Content-Type': 'application/json'})
  # Making the request
  f = urllib2.urlopen(req)
  if f.getcode() != 200:
    print f.read()


# Get the environment variables
PR_NUMBER = os.environ.get('TRAVIS_PULL_REQUEST')
BUILD_ID = os.environ.get('TRAVIS_BUILD_ID')

# Read the test result output from stdin
test_result = sys.stdin.read().strip()
# Populate the template text
comment = (
"The [build]"
"(https://travis-ci.org/tldr-pages/tldr/builds/{build_id})"
" for this PR has failed with the following message:"
"\n```\n"
"{comment_body}"
"\n```\n"
"Please fix the error(s) and push again."
).format(build_id=BUILD_ID, comment_body=test_result)

# If its a PR, post a comment on it
if PR_NUMBER != "false":
  post_comment(PR_NUMBER, comment)
