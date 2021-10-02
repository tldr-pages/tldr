# ssh-agent

> Spawn an SSH Agent process.
> An SSH Agent holds SSH keys decrypted in memory until removed or the process is killed.
> See also `ssh-add`, which can add and manage keys held by an SSH Agent.
> More information: <https://man.openbsd.org/ssh-agent>.

- Start an SSH Agent for the current shell:

`eval $(ssh-agent)`

- Kill the currently running agent:

`ssh-agent -k`
