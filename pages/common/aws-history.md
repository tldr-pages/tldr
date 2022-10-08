# aws history

> Commands to interact with the history of AWS CLI commands ran over time (the record of history of AWS CLI commands must be enabled).
> More information: <https://docs.aws.amazon.com/cli/latest/reference/history/>.

- List commands history with command IDs:

`aws history list`

- Display events related to a specific command given a command ID:

`aws history show {{command_id}}`
