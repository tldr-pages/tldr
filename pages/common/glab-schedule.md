# glab schedule

> Manage GitLab CI/CD pipeline schedules.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/schedule/_index.md>.

- List pipeline schedules for the current repository:

`glab schedule list`

- List pipeline schedules for a specific repository:

`glab schedule list {{[-R|--repo]}} {{owner}}/{{repository}}`

- Create a new pipeline schedule:

`glab schedule create --cron "{{cron_pattern}}" --description "{{description}}" --ref "{{branch}}"`

- Create a pipeline schedule with variables:

`glab schedule create --cron "{{cron_pattern}}" --description "{{description}}" --ref "{{branch}}" --variable "{{key}}:{{value}}"`

- Trigger a pipeline schedule to run immediately:

`glab schedule run {{schedule_id}}`

- Update the cron interval of a pipeline schedule:

`glab schedule update {{schedule_id}} --cron "{{cron_pattern}}"`

- Enable or disable a pipeline schedule:

`glab schedule update {{schedule_id}} --active={{true|false}}`

- Delete a pipeline schedule:

`glab schedule delete {{schedule_id}}`
