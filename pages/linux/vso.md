# vso

> Utility to perform maintenance tasks on Vanilla OS.
> More information: <https://github.com/Vanilla-OS/vanilla-system-operator>.

- Trigger a system update immediately:

`sudo vso trigger-update --now`

- Create an automated task upon an application's launch:

`vso create-task --name "{{string}}" --description {{string}} --{{command|on-condition-command}} "{{cmd}}" --on-process {{process}}`

- Create an automated task to execute during boot:

`vso create-task --name "{{string}}" --description {{string}} --command "{{cmd}}" --on-boot`

- Create an automated task to execute during specific battery states:

`vso create-task --name "{{string}}" --description {{string}} --command "{{cmd}}" --{{on-low-battery|on-charge|on-battery|on-full-battery}}`

- Create an automated task to execute [at] a specific time interval (hh: mm) or re-execute it [every] time after specific time intervals (m,h,d):

`vso create-task --name "{{string}}" --description {{string}} --command "{{cmd}}" --{{at|every}} "{{time_interval}}"`

- Create an automated task which asks for a confirmation before execution:

`vso create-task --name "{{string}}" --description {{string}} --command "{{cmd}}" --need-confirm`

- Create an automated task to execute during network connection or disconnection:

`vso create-task --name "{{string}}" --description {{string}} --command "{{cmd}}" --{{on-network|on-disconnect}}`

- Delete an automated task:

`vso delete-task "{{task}}"`
