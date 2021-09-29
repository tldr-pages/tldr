# sshd

> Secure Shell Daemon - allows remote machines to securely log in to the current machine.
> Remote machines can execute commands as it is executed at this machine.
> More information: <https://man.openbsd.org/sshd>.

- Start Daemon and run in the background:

`sshd`

- Start Daemon and keep foreground:

`sshd -D`

- Start Daemon and show logging details:

`sshd -D -d`

- Run on another port:

`sshd -p {{port}}`
