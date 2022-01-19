# glab auth

> Authenticate with a GitLab host from the command-line.
> More information: <https://glab.readthedocs.io/en/latest/auth>.

- Log in with interactive prompt:

`glab auth login`

- Log in with a token (created in https://gitlab.com/-/profile/personal_access_tokens):

`glab auth login --token {{your_token}}`

- Check authentication status:

`glab auth status`

- Log in to a specific GitLab instance:

`glab auth login --hostname {{gitlab.example.com}}`
