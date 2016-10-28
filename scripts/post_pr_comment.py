import json
import os
import urllib2

GITHUB_URL = 'https://api.github.com'

def post_comment(pr_id, repo_slug, comment_body, user_token):
	url = '{api_url}/repos/{slug}/issues/{number}/comments'.format(
        api_url=GITHUB_URL, slug=repo_slug, number=pr_id)
	req = urllib2.Request(url=url,
                       data=json.dumps({'body': comment_body}))
	req.add_header('Authorization', 'token ' + user_token)
	f = urllib2.urlopen(req)
	if f.getcode() != 201:
		print f.read()


if __name__ == '__main__':
	PR_NUMBER = os.environ.get('TRAVIS_PULL_REQUEST')
	REPO_SLUG = os.environ.get('TRAVIS_REPO_SLUG') # owner_name/repo_name
	TEST_RESULT = os.environ.get('TRAVIS_TEST_RESULT')
	BOT_TOKEN = os.environ.get('TRAVIS_BOT_GITHUB_TOKEN')

	comment = (
        """
The PR has failed with the following message -
```
{comment_body}
```
Please rectify the error and make another push.
        """).format(comment_body=TEST_RESULT)

	if PR_NUMBER != "false":
		post_comment(PR_NUMBER, REPO_SLUG, comment, BOT_TOKEN)