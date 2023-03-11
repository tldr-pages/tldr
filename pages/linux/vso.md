# vso

> Utility to perform maintenance tasks on Vanilla OS.
> More information: <https://github.com/Vanilla-OS/vanilla-system-operator>.

- Trigger a system update immediately:

`sudo vso trigger-update --now`

- Check for package updates and list them:

`sudo vso update-check`

- Create an automated task upon an application's launch:

`vso create-task --name "{{string}}" --description "{{string}}" --{{command|on-condition-command}} "{{command}}" --on-process {{integer}}`

- Create an automated task to execute during boot:

`vso create-task --name "{{string}}" --description "{{string}}" --command "{{command}}" --on-boot`

- Create an automated task to execute during specific battery states:

`vso create-task --name "{{string}}" --description "{{string}}" --command "{{command}}" --{{on-low-battery|on-charge|on-battery|on-full-battery}}`

- Create an automated task which asks for a confirmation before execution:

`vso create-task --name "{{string}}" --description "{{string}}" --command "{{command}}" --need-confirm`

- Create an automated task to execute during network connection or disconnection:

`vso create-task --name "{{string}}" --description "{{string}}" --command "{{command}}" --{{on-network|on-disconnect}}`

- Delete an automated task:

`vso delete-task "{{task}}"`
