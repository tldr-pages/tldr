# gitlab-runner

> Run GitLab CI jobs.
> More information: <https://docs.gitlab.com/runner/>.

- Register a runner:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}}`

- Register a runner with a Docker executor:

`sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}} --executor {{docker}}`

- Unregister a runner:

`sudo gitlab-runner unregister --name {{name}}`

- Display the status of the runner service:

`sudo gitlab-runner status`

- Restart the runner service:

`sudo gitlab-runner restart`

- Verify registered runners are running:

`sudo gitlab-runner verify`
