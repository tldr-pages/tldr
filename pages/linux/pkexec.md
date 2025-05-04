# pkexec

> Execute commands as another user.
> Asks for password in a GUI if available.
> More information: <https://polkit.pages.freedesktop.org/polkit/pkexec.1.html>.

- Run command as root:

`pkexec {{command}}`

- Switch user to root:

`pkexec`

- Run command as a specific user:

`pkexec --user {{username}} {{command}}`
