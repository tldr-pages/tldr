# chronyc

> Query the Chrony NTP daemon.

- Start chronyc in interactive mode:

`chronyc`

- Display tracking stats for chrony daemon:

`chronyc tracking`

- Print time sources chrony is currently using as a time source:

`chronyc sources`

- Display stats for sources currently used by chrony daemon as a time source:

`chronyc sourcestats`

- Step system clock immediately, bypassing any slewing:

`chronyc makestep`

- Display verbose information about each ntp source:

`chronyc ntpdata`
