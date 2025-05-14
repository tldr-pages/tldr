# keyd

> Remap keys.
> More information: <https://manned.org/keyd>.

- Start and enable the `keyd` service:

`systemctl enable keyd --now`

- Display keypress information:

`sudo keyd monitor`

- Reset bindings and reload the configuration files in `/etc/keyd`:

`sudo keyd reload`

- List all valid key names:

`keyd list-keys`

- Create a temporary binding:

`sudo keyd bind "{{pressed_key}} = {{output_key}}`
