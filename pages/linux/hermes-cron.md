# hermes cron

> Manage scheduled cron jobs for recurring tasks and automated workflows.
> More information: <https://hermes-agent.nousresearch.com/docs>.

- List all cron jobs:

`hermes cron list`

- Create a new cron job with a schedule and prompt:

`hermes cron create --schedule "0 9 * * *" --prompt "Send a morning briefing"`

- Create a recurring job every 30 minutes:

`hermes cron create --schedule "30m" --prompt "Check system health"`

- Create a job with attached skills:

`hermes cron create --schedule "daily" --prompt "Generate news digest" --skills news-digest-umbrella`

- Pause a cron job:

`hermes cron pause {{job_id}}`

- Resume a paused cron job:

`hermes cron resume {{job_id}}`

- Remove a cron job:

`hermes cron remove {{job_id}}`

- Run a cron job immediately:

`hermes cron run {{job_id}}`
