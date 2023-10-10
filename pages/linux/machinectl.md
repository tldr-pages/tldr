# Machinectl

> Machinectl is a command-line utility for managing Linux containers, particularly on systems that use the systemd init system.
> It provides a powerful and convenient way to create, start, stop, and manage container instances, referred to as "machines" in systemd terminology.

- Create a Machine:

`sudo machinectl create my-container`

- You can start a container with the following command:

`sudo machinectl start my-container`

- To stop a running container, use the following command:

`sudo machinectl stop my-container`

- To see a list of running containers, execute:

`machinectl list`

- To log into a container for interactive use, use:

`sudo machinectl shell my-container`

- Machinectl is typically available on systems that support systemd. If not installed, you can usually obtain it via your distribution's package manager. For example, on Debian/Ubuntu:

`sudo apt-get install systemd-container`
