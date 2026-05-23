# bitsadmin

> Create, download, upload, and manage BITS transfer jobs.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin>.

- Transfer a file using a new download job:

`bitsadmin /transfer {{job_name}} {{https://example.com/file.zip}} {{C:\path\to\file.zip}}`

- Create a new download job:

`bitsadmin /create {{job_name}}`

- Add a file to a job:

`bitsadmin /addfile {{job_name}} {{https://example.com/file.zip}} {{C:\path\to\file.zip}}`

- Resume a job in the transfer queue:

`bitsadmin /resume {{job_name}}`

- Complete a job after it reaches the `TRANSFERRED` state:

`bitsadmin /complete {{job_name}}`
