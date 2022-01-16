# ssh

> Secure Shell is a protocol used to securely log onto remote systems.
> It can be used for logging or executing commands on a remote server.
> More information: <https://man.openbsd.org/ssh>.

- Connect to a remote server:

`ssh {{username}}@{{remote_host}}`

- Connect to a remote server with a specific identity (private key):

`ssh -i {{path/to/key_file}} {{username}}@{{remote_host}}`

- Connect to a remote server using a specific port:

`ssh {{username}}@{{remote_host}} -p {{2222}}`

- Run a command on a remote server with a [t]ty allocation allowing interaction with the remote command:

`ssh {{username}}@{{remote_host}} -t {{command}} {{command_arguments}}`

- SSH tunneling: Dynamic port forwarding (SOCKS proxy on `localhost:1080`):

`ssh -D {{1080}} {{username}}@{{remote_host}}`

- SSH tunneling: Forward a specific port (`localhost:9999` to `example.org:80`) along with disabling pseudo-[T]ty allocation and executio[N] of remote commands:

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{username}}@{{remote_host}}`

- SSH jumping: Connect through a jumphost to a remote server (Multiple jump hops may be specified separated by comma characters):

`ssh -J {{username}}@{{jump_host}} {{username}}@{{remote_host}}`

- Agent forwarding: Forward the authentication information to the remote machine (see `man ssh_config` for available options):

`ssh -A {{username}}@{{remote_host}}`
