# login

> Initiates a session for a user.
> More information: <https://manned.org/login>.

- Log in as a user:

`login {{user}}`

- Log in as user without authentication if user is preauthenticated:

`login -f {{user}}`

- Log in as user and preserve environment:

`login -p {{user}}`

- Log in as a user on a remote host:

`login -h {{host}} {{user}}`
