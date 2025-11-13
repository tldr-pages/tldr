# koji cancel

> Cancel one or more running Koji tasks.
> More information: <https://docs.pagure.org/koji/>.

- Cancel a task by its ID:
`koji cancel {{task_id}}`

- Cancel multiple tasks:
`koji cancel {{task_id1}} {{task_id2}}`

- Cancel a task with verbose output:
`koji --verbose cancel {{task_id}}`

- Display help:
`koji cancel --help`
