# ausearch

> Query the Linux audit log for events.
> Part of the `audit` package.
> See also: `audit2why`, `audit2allow`, `aureport`.
> More information: <https://manned.org/ausearch>.

- Search for all SELinux AVC denial events:

`sudo ausearch -m avc`

- Search for events related to a specific executable:

`sudo ausearch -c {{httpd}}`

- Search for events from a specific user:

`sudo ausearch -ui {{1000}}`

- Search for events in the last 10 minutes:

`sudo ausearch -ts recent`

- Search for failed login attempts:

`sudo ausearch -m user_login -sv no`

- Search for events related to a specific file:

`sudo ausearch -f {{path/to/file}}`

- Display results in raw format for further processing:

`sudo ausearch -m avc --raw`
