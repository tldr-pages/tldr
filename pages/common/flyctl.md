# flyctl

> Command-line tool for flyctl.io.
> More information: <https://github.com/superfly/flyctl>.

- Sign into fly account:

`flyctl auth login`

- Launch from your own Dockerfile (Default path is current working directory):

`flyctl launch --dockerfile {{path/to/Dockerfile}}`

- Open browser to current deployed application:

`flyctl open`

- Deploy Fly applications:

`flyctl deploy --dockerfile {{path/to/Dockerfile}}`

- Open web browser on Fly Web UI for this app:

`flyctl dashboard`

- List apps:

`flyctl apps list`

- View app status:

`flyctl status -app {{app_name}}`

- Show version information:

`flyctl version`
