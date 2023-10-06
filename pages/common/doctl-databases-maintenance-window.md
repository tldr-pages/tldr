# doctl databases maintenance-window

> Manage specific databases that are served by a database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window/>.

- Run a doctl databases maintenance-window command with an access token:

`doctl databases maintenance-window [command] --access-token {{ access_token }}`

- Retrieve details about a database cluster's maintenance windows:

`doctl databases maintenance-window get {{ database id }}`

- Update the maintenance window for a database cluster:

`doctl databases maintenance-window update {{ database id }} --day {{ day of the week (e.g. monday) }} --hour {{ 24 hour (e.g. '16:00') }}`