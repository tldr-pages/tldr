# chronyc

> Query the Chrony NTP daemon.
> More information: <https://chrony.tuxfamily.org/doc/4.0/chronyc.html>.

- Start `chronyc` in interactive mode:

`chronyc`

- Display tracking stats for the Chrony daemon:

`chronyc tracking`

- Print the time sources that Chrony is currently using:

`chronyc sources`

- Display stats for sources currently used by chrony daemon as a time source:

`chronyc sourcestats`

- Step the system clock immediately, bypassing any slewing:

`chronyc makestep`

- Display verbose information about each NTP source:

`chronyc ntpdata`
