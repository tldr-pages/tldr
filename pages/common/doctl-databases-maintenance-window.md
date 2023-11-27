# doctl databases maintenance-window

> Schedule, and check the schedule of, maintenance windows for your databases.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window>.

- Run a `doctl databases maintenance-window` command with an access token:

`doctl databases maintenance-window {{command}} --access-token {{access_token}}`

- Retrieve details about a database cluster's maintenance windows:

`doctl databases maintenance-window get {{database_id}}`

- Update the maintenance window for a database cluster:

`doctl databases maintenance-window update {{database_id}} --day {{day_of_the_week}} --hour {{hour_in_24_hours_format}}`
