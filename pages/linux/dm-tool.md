# dm-tool

> A tool to commnicate with the display manager. EG: lock currect session and show lightdm, list all open sessions, connect an existing x server to the display manager.
> More information: <https://manned.org/dm-tool>.

- Show the greeter while keeping current desktop session open and waiting to be restored upon authentication by logged in user:

`dm-tool switch-to-greeter`

- Lock the current session:

`dm-tool lock`

- Swicth user, showing a authentication prompt if required:

`dm-tool switch-to-user {{username}} [{{session}}]`

- Add a new X server instance:

`dm-tool add-seat [{{name}}={{value}}]`
