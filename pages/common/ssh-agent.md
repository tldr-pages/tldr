# ssh-agent

> Spawn an ssh-agent process.
> The ssh-agent will hold your ssh key decrypted in memory until evicted.
> Add and manage keys with `ssh-add`.

- Start an SSH Agent for the current shell:

`eval $(ssh-agent)`

- Kill the currently running agent:

`ssh-agent -k`

- Manually connect to an existing agent (rare):

`export SSH_AUTH_SOCK={{ssh-agent socket}}`
`export SSH_AGENT_PID={{ssh-agent pid}}`
