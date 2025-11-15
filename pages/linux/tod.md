# tod

> A tiny Todoist client in Rust.
> It takes simple input and dumps it in your inbox or another project. Taking advantage of natural language processing to assign due dates, tags, etc.
> More information: <https://github.com/alanvardy/tod>.

- Import your projects (this is necessary to enable project prompts):

`tod project import`

- Quickly create a task with due date:

`tod --quickadd {{Buy more milk today}}`

- Create a new task (you will be prompted for content and project):

`tod task create`

- Create a task in a project:

`tod task create --content "{{Write more rust}}" --project {{code}}`

- Get the next task for a project:

`tod task next`

- Get your work schedule:

`tod task list --scheduled --project {{work}}`

- Get all tasks for work:

`tod task list --project {{work}}`
