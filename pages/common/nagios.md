# nagios

> Legacy host/service/networking monitoring program.
> Largely deprecated by `nagios4`.
> See also: `nagios2`, `nagios3`, `nagios4`.
> More information: <https://manned.org/nagios>.

- Start `nagios`:

`nagios /etc/nagios/nagios.cfg`

- Start `nagios` in daemon mode:

`nagios -d`

- Start `nagios`, print service check scheduling information to `stdout`, then shutdown:

`nagios -s`

- Verify configuration file:

`nagios -v`
