# koji resubmit

> Retry a canceled or failed task, using the same parameter as the original task.
> More information: <https://docs.pagure.org/koji>.

- Resubmit task:

`koji resubmit {{task_id}}`

- Don't wait on task:

`koji resubmit {{task_id}} --nowait`

- Don't print the task information:

`koji resubmit {{task_id}} --quiet`

- Display help:

`koji resubmit {{[-h|--help]}}`
