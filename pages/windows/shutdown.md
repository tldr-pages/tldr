# shutdown

> A tool for shutting down, restarting or logging off a machine.

- Shutdown the current machine:

`shutdown /s`

- Restart the current machine:

`shutdown /r`

- Hibernate the current machine:

`shutdown /h`

- Log off the current machine:

`shutdown /l`

- Specify a timeout in seconds to wait before shutting down:

`shutdown /s /t {{seconds}}`

- Specify a comment for the shutdown reason:

`shutdown /s /c "{{reason}}"`

- Abort a shutdown sequence whose timeout is yet to expire:

`shutdown /a`

- Shutdown a remote machine:

`shutdown /m {{\\hostname}}`
