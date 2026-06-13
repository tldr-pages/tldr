# hermes logs

> View and filter Hermes log files including agent logs and error logs.
> More information: <https://hermes-agent.nousresearch.com/docs>.

- View the last 50 lines of agent.log:

`hermes logs`

- Follow agent.log in real time:

`hermes logs -f`

- View errors.log:

`hermes logs errors`

- Show lines from the last hour:

`hermes logs --since 1h`

- Show lines from the last 24 hours:

`hermes logs --since 24h`

- Show lines from the last 7 days:

`hermes logs --since 7d`
