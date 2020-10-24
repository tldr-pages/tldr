# autossh

> Runs, monitors and restarts SSH connections.
> Auto-reconnects to keep port forwarding tunnels up. Accepts all ssh flags.
> More information: <https://harding.motd.ca/autossh>.

- Open an SSH session, restarting when a monitoring port fails return data:

`autossh -M {{monitor_port}} {{ssh_command}}`

- Open an SSH session which forwards a local port to a remote one, restarting if necessary:

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Fork before executing ssh (runs in the background) and don't open a remote shell:

`autossh -f -M {{monitor_port}} -N {{ssh_command}}`

- Run autossh in the background, with no monitoring port, instead relying on SSH keep-alives every 10 seconds to detect failure:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" {{ssh_command}}`

- Run autossh in the background, with no monitoring port, no remote shell, exiting if the port forward fails:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Run autossh in the background with debug output logged to a file and ssh verbose output logged to a second file:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{log_file}} autossh -f -M {{monitor_port}} -v -E {{ssh_log_file}} {{ssh_command}}`
