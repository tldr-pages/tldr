# eventcreate

> Create custom entries in the event log.

- Create a new event in the log:

`eventcreate /t {{success|error|warning|information}} /id {{id}} /d "{{message}}"`

- Create an event in a specific event log:

`eventcreate /l {{log_name}} /t {{type}} /id {{id}} /d "{{message}}"`

- Create an event with a specific source:

`eventcreate /so {{source_name}} /t {{type}} /id {{id}} /d "{{message}}"`

- Create an event in a remote machine's event log:

`eventcreate /s {{hostname}} /u {{username}} /p {{password}} /t {{type}} /id {{id}} /d "{{message"}}`
