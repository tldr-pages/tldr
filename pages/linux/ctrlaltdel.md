# ctrlaltdel

> Utility to control what happens when CTRL+ALT+DEL is pressed.
> More information: <https://manned.org/ctrlaltdel>.

- Get current setting:

`ctrlaltdel`

- Set CTRL+ALT+DEL to reboot immediately, without any preparation:

`sudo ctrlaltdel hard`

- Set CTRL+ALT+DEL to reboot "normally", giving processes a chance to exit first (send SIGINT to PID1):

`sudo ctrlaltdel soft`
