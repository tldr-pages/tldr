# dnf-automatic

> A tool for automating the checking, downloading, and/or applying package updates via dnf.
> More information: <https://dnf.readthedocs.io/en/latest/automatic.html>.

- Override config file and only notify of available updates:

`systemctl enable --now dnf-automatic-notifyonly.timer`

- Run with default config file:

`systemctl enable --now dnf-automatic.timer`

- Use dnf-automatic in a custom systemd timer:

`/usr/bin/dnf-automatic /path/to/automatic.conf --timer`
