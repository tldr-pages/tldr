# dm-tool
A tool to commnicate with the lightdm display manager. EG: lock currect session and show lightdm, list all open sessions, connect an existing x server to the display manager.
More informatioin: https://www.mankier.com/1/dm-tool.

- show the greeter while keeping current desktop session in ram and waiting to be restored upon autentication by logged in uuser
`dm-tool switch-to-greeter`

- swicth user, showing a authentication prompt if required
`dm-tool swict-to-user {{username}} [{{session}}]`

- lock the current session
`dm-tool lock`

- add a new X server instance
`dm-tool add-seat [{{name}}={{value}}]`