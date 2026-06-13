# koji cancel

> Cancel active tasks running on the Koji build system.
> More information: <https://docs.pagure.org/koji/>.

- Cancel a task by its ID:

`koji cancel {{task_id}}`

- Cancel multiple tasks:

`koji cancel {{task_id1 task_id2 ...}}`

- Cancel a task with verbose output:

`koji cancel --verbose {{task_id}}`

- Display help:

`koji cancel {{[-h|--help]}}`
