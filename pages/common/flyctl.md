# flyctl

> Command-line tool for flyctl.io.
> More information: <https://github.com/superfly/flyctl>.

- Sign into a Fly account:

`flyctl auth login`

- Launch an application from a specific Dockerfile (the default path is the current working directory):

`flyctl launch --dockerfile {{path/to/dockerfile}}`

- Open the current deployed application in the default web browser:

`flyctl open`

- Deploy the Fly applications from a specific Dockerfile:

`flyctl deploy --dockerfile {{path/to/dockerfile}}`

- Open the Fly Web UI for the current application in a web browser:

`flyctl dashboard`

- List all applications in the logged-in Fly account:

`flyctl apps list`

- View the status of a specific running application:

`flyctl status --app {{app_name}}`

- Show version information:

`flyctl version`
