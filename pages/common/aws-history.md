# aws history

> Commands to interact with the history of AWS CLI commands ran over time (the record of history of AWS CLI commands must be enabled).
> More information: <https://docs.aws.amazon.com/cli/latest/reference/history/>.

- Get a list of previously run commands and their command ids:

`aws history list`

- Get the various events related to running a specific CLI command with its command id:

`aws history show {{1affe293-ed81-451c-a044-ea99223a93bf}}`
