# init

> Linux run level manager.
> Requires the SYSVINIT compile-time option to be enabled if using systemd.
> More information: <https://manned.org/init.8>.

- Set the system to run a graphical environment:

`sudo init 5`

- Set the system to run multiuser terminal:

`sudo init 3`

- Shut down the system:

`init 0`

- Reboot the system:

`init 6`

- Set the system to run on terminal with only root user allowed and no networking:

`sudo init 1`
