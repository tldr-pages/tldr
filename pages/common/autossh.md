# autossh

> Run, monitor and restart SSH connections.
> Auto-reconnects to keep port forwarding tunnels up. Accepts all `ssh` flags.
> More information: <https://www.harding.motd.ca/autossh>.

- Start an SSH session, restarting when the [M]onitoring port fails to return data:

`autossh -M {{monitor_port}} "{{ssh_command}}"`

- Forward a [L]ocal port to a remote one, restarting when necessary:

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Fork `autossh` into the background before executing `ssh` and do [N]ot open a remote shell:

`autossh -f -M {{monitor_port}} -N "{{ssh_command}}"`

- Run in the background, with no monitoring port, and instead send SSH keep-alive packets every 10 seconds to detect failure:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_command}}"`

- Run in the background, with no monitoring port and no remote shell, exiting if the port forward fails:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Run in the background, logging `autossh` debug output and `ssh` verbose output to files:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{path/to/autossh_log_file.log}} autossh -f -M {{monitor_port}} -v -E {{path/to/ssh_log_file.log}} {{ssh_command}}`
