# zeroclaw cron

> Manage scheduled tasks for ZeroClaw.
> More information: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- List all scheduled tasks:

`zeroclaw cron list`

- Add a new scheduled task with a cron expression:

`zeroclaw cron add "{{* * * * *}}" "{{command}}"`

- Add a one-shot delayed task:

`zeroclaw cron once {{30m|1h|1d|...}} "{{command}}"`

- Remove a scheduled task:

`zeroclaw cron remove {{task_id}}`

- Pause a scheduled task:

`zeroclaw cron pause {{task_id}}`

- Resume a paused task:

`zeroclaw cron resume {{task_id}}`

- Display help:

`zeroclaw cron {{[-h|--help]}}`
