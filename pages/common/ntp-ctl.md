# ntp-ctl

> Management client for the `ntpd-rs` daemon.
> More information: <https://docs.ntpd-rs.pendulum-project.org/man/ntp-ctl.8>.

- Display information about the current state of the NTP daemon:

`ntp-ctl status`

- Check if the specified configuration file (default: `/etc/ntpd-rs/ntp.toml`) is valid:

`ntp-ctl {{[-c|--config]}} {{path/to/config}} validate`

- Interactively run a single synchronization of the clock:

`sudo ntp-ctl force-sync`
