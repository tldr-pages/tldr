# bitsadmin

> Create download or upload jobs and monitor their progress with Background Intelligent Transfer Service (BITS).
> A job is identified by its display name or GUID. Display names do not have to be unique.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/bitsadmin>.

- Transfer a file at normal priority (the job is completed when the transfer succeeds):

`bitsadmin /transfer {{job_name}} /download /priority normal {{https://example.com/file.zip}} {{path\to\file.zip}}`

- Create a suspended download job:

`bitsadmin /create {{job_name}}`

- Add a file to a job:

`bitsadmin /addfile {{job_name}} {{https://example.com/file.zip}} {{path\to\file.zip}}`

- Activate a suspended job:

`bitsadmin /resume {{job_name}}`

- Show the state of a job, including files and errors:

`bitsadmin /info {{job_name}} /verbose`

- Make the transferred files available once the state is `TRANSFERRED`:

`bitsadmin /complete {{job_name}}`

- List jobs in the transfer queue:

`bitsadmin /list`

- Remove a job and delete its temporary files:

`bitsadmin /cancel {{job_name}}`
