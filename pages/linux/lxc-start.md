# lxc-start

> Start a container.
> More information: <https://linuxcontainers.org/lxc/getting-started/>.

- Start the lxc service:

`systemctl start lxc-net`

- Start a container:

`sudo lxc-start {{container_name}}`

- Start a container in the foreground:

`sudo lxc-start {{container_name}} {{[-F|--foreground]}}`

- Exit out of a foreground container (run this in a separate terminal):

`sudo lxc-stop {{container_name}}`

- Write debug logs to a file:

`sudo lxc-start {{container_name}} {{[-l|--logpriority]}} DEBUG {{[-o|--logfile]}} {{path/to/logfile}}`

- Display help:

`lxc-start {{[-?|--help]}}`
