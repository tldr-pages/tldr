# vagrant ssh

> Open an SSH session to a Vagrant-managed machine.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/ssh>.

- SSH into the default machine:
`vagrant ssh`

- SSH into a specific machine by name:
`vagrant ssh {{machine_name}}`

- Execute a single command over SSH and exit:
`vagrant ssh --command "{{uname -a}}"`

- Connect without automatic authentication:
`vagrant ssh --plain`

- Pass additional flags directly to the underlying SSH client:
`vagrant ssh -- -L {{localhost:8080:localhost:80}}`
