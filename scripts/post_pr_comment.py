import json
import os
import sys
import urllib2

GITHUB_URL = 'https://api.github.com'

def post_comment(pr_id, repo_slug, comment_body, user_token):
	# Constructing the url
	url = '{api_url}/repos/{slug}/issues/{number}/comments'.format(
        api_url=GITHUB_URL, slug=repo_slug, number=pr_id)
	req = urllib2.Request(url=url,
                       data=json.dumps({'body': comment_body}))
	req.add_header('Authorization', 'token ' + user_token)
	# Making the request
	f = urllib2.urlopen(req)
	if f.getcode() != 201:
		print f.read()


# Get the environment variables
PR_NUMBER = os.environ.get('TRAVIS_PULL_REQUEST')
REPO_SLUG = os.environ.get('TRAVIS_REPO_SLUG') # owner_name/repo_name
BOT_TOKEN = os.environ.get('TRAVIS_BOT_GITHUB_TOKEN')
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
	post_comment(PR_NUMBER, REPO_SLUG, comment, BOT_TOKEN)
