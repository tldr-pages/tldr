# init

> Linux run level manager.
> Requires the SYSVINIT compile-time option to be enabled if using systemd.
> More information: <https://manned.org/init>.

- Set the system to run a graphical environment:

`init 5`

- Set the system to run multiuser terminal:

`init 3`

- Shut down the system:

`init 0`

- Reboot the system:

`init 6`

- Set the system to run on terminal with only root user allowed an no networking:

`init 1`
