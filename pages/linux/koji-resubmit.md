# koji resubmit

> Retry a canceled or failed task, using the same parameter as the original task.
> More information: <https://docs.pagure.org/koji>.

- Resubmit a task:

`koji resubmit {{task_id}}`

- Resubmit a task without waiting for it to finish:

`koji resubmit {{task_id}} --nowait`

- Resubmit a task without printing task information:

`koji resubmit {{task_id}} --quiet`

- Display help:

`koji resubmit {{[-h|--help]}}`
