# pivpn

> Easy security-hardened OpenVPN setup and manager.
> Originally designed for the Raspberry Pi, but works on other Linux devices too.
> Homepage: <http://www.pivpn.io/>.

- Install PiVPN:

`curl -L https://install.pivpn.io | bash`

- Add a new client device:

`sudo pivpn add`

- List all client devices:

`sudo pivpn list`

- List currently connected devices and their statistics:

`sudo pivpn clients`

- Revoke a previously authed device:

`sudo pivpn revoke`

- Uninstall PiVPN:

`sudo pivpn uninstall`
