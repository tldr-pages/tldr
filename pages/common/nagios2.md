# nagios2

> Legacy host/service/networking monitoring program.
> Largely deprecated by `nagios4`.
> See also: `nagios`, `nagios3`, `nagios4`.
> More information: <https://manned.org/nagios>.

- Start `nagios2`:

`nagios2 /etc/nagios2/nagios.cfg`

- Start `nagios2` in daemon mode:

`nagios2 -d`

- Start `nagios2`, print service check scheduling information to `stdout`, then shutdown:

`nagios2 -s`

- Verify configuration file:

`nagios2 -v`
