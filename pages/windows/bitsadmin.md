# bitsadmin

> Command-line tool to manage and monitor Background Intelligent Transfer Service (BITS) jobs.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin>.

- Download a file from a URL to a local path:

`bitsadmin /transfer {{job_name}} /download /priority {{normal}} {{http://example.com/file.zip}} {{C:\path\to\file.zip}}`

- Create a download job and add files to it:

`bitsadmin /create {{job_name}} && bitsadmin /addfile {{job_name}} {{http://example.com/file.zip}} {{C:\path\to\file.zip}}`

- Resume a job in the queue:

`bitsadmin /resume {{job_name}}`

- Display information about a specific job:

`bitsadmin /info {{job_name}} /verbose`

- Monitor the transfer queue and refresh every 5 seconds:

`bitsadmin /monitor /refresh {{5}}`

- List all jobs for the current user:

`bitsadmin /list`

- Complete a job (transitions to the transferred state):

`bitsadmin /complete {{job_name}}`

- Cancel a job and remove it from the queue:

`bitsadmin /cancel {{job_name}}`
