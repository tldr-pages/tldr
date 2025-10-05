# ausearch

> Query the Linux audit log for events.
> Part of the `audit` package.
> See also: `audit2why`, `audit2allow`, `aureport`.
> More information: <https://manned.org/ausearch>.

- Search for all SELinux AVC denial events:

`sudo ausearch {{[-m|--message]}} avc`

- Search for events related to a specific executable:

`sudo ausearch {{[-c|--comm]}} {{httpd}}`

- Search for events from a specific user:

`sudo ausearch {{[-ui|--uid]}} {{1000}}`

- Search for events in the last 10 minutes:

`sudo ausearch {{[-ts|--start]}} recent`

- Search for failed login attempts:

`sudo ausearch {{[-m|--message]}} user_login {{[-sv|--success]}} no`

- Search for events related to a specific file:

`sudo ausearch {{[-f|--file]}} {{path/to/file}}`

- Display results in raw format for further processing:

`sudo ausearch {{[-m|--message]}} avc --raw`
