# guacd

> Apache Guacamole proxy daemon.
> Support loader for client plugins to interface between the Guacamole protocol and any arbitrary remote desktop protocol (e.g. RDP, VNC, Other).
> More information: <https://guacamole.apache.org/>.

- Bind guacd at specific port on localhost:

`guacd -b {{127.0.0.1}} -l {{4823}}`

- Start guacd in debug mode and keep in the foreground for troubleshooting:

`guacd -f -L {{debug}}`

- Use guacd with SSL enabled:

`guacd -C {{my-cert.crt}} -K {{my-key.pem}}`

- Write PID of guacd instance to a file for automating init scripts:

`guacd -p {{/var/run/guacd.pid}}`
