# znc

> IRC bouncer.
> More information: <https://manned.org/znc>.

- Run the initial setup:

`znc {{[-c|--makeconf]}}`

- Start the IRC bouncer daemon:

`znc`

- Setup `znc` for systemd:

`sudo {{[-u|--user]}} znc znc {{[-c|--makeconf]}} {{[-d|--datadir]}} /var/lib/znc`

- Enable `znc` to start on boot and start it now:

`systemctl enable znc --now`
