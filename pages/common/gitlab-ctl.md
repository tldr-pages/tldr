# gitlab-ctl

> CLI tool for managing the GitLab omnibus.
> More information: <https://docs.gitlab.com/omnibus/maintenance/>.

- Check the status of every service:

`sudo gitlab-ctl status`

- Check the status of a specific service:

`sudo gitlab-ctl status {{nginx}}`

- Restart every service:

`sudo gitlab-ctl restart`

- Restart a specific service:

`sudo gitlab-ctl restart {{nginx}}`

- Get the logs of every service:

`sudo gitlab-ctl tail`

- Get the logs of a specific service:

`sudo gitlab-ctl tail {{nginx}}`
