# eventcreate

> Create custom entries in the event log.
> Event IDs can be any number between 1 and 1000.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/eventcreate>.

- Create a new event with a given ID (1-1000) in the log:

`eventcreate /t {{success|error|warning|information}} /id {{id}} /d "{{message}}"`

- Create an event in a specific event log:

`eventcreate /l {{log_name}} /t {{type}} /id {{id}} /d "{{message}}"`

- Create an event with a specific source:

`eventcreate /so {{source_name}} /t {{type}} /id {{id}} /d "{{message}}"`

- Create an event in a remote machine's event log:

`eventcreate /s {{hostname}} /u {{username}} /p {{password}} /t {{type}} /id {{id}} /d "{{message}}"`
