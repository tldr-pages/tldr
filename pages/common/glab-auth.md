# glab auth

> Authenticate with a GitLab host from the command-line.
> More information: <https://glab.readthedocs.io/en/latest/auth/>.

- Log in with interactive prompt:

`glab auth login`

- Log in with a token from standard input (created in https://gitlab.com/-/profile/personal_access_tokens):

`echo {{your_token}} | glab auth login --stdin`

- Check if you are logged in:

`glab auth status`

- Log in to a specific GitLab instance:

`glab auth login --hostname {{gitlab.example.com}}`
