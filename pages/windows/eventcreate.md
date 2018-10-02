# eventcreate

> Create custom entries in the event log.

- Create an event with a specific type:

`eventcreate /t {{success|error|warning|information}} /id {{id}} /d "{{message}}"`

- Create an event in a specific event log:

`eventcreate /l {{log_name}} /t {{event_type}} /id {{event_id}} /d "{{message}}"`

- Create an event with a specific source:

`eventcreate /so {{source_name}} /t {{event_type}} /id {{event_id}} /d "{{message}}"`

- Create an event for a remote machine:

`eventcreate /s {{hostname}} /u {{username}} /p {{password}} /d "{{message"}}`
