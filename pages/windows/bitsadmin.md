# bitsadmin

> Manage Background Intelligent Transfer Service (BITS) jobs.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin>.

- List all BITS jobs owned by the current user:

`bitsadmin /list`

- List all BITS jobs for all users:

`bitsadmin /list /allusers`

- Download a file from a URL to a local destination in one step:

`bitsadmin /transfer {{job_name}} {{https://example.com/file.zip}} {{C}}:{{path\to\destination_file.zip}}`

- Create a new download job:

`bitsadmin /create {{job_name}}`

- Add a file to an existing job:

`bitsadmin /addfile {{job_name}} {{https://example.com/file.zip}} {{C}}:{{path\to\destination_file.zip}}`

- Resume a paused or suspended job:

`bitsadmin /resume {{job_name}}`

- Display detailed information about a specific job:

`bitsadmin /info {{job_name}} /verbose`

- Complete and finalize a finished job:

`bitsadmin /complete {{job_name}}`
