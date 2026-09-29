# nagios

> Legacy host/service/networking monitoring program.
> Note: This command is deprecated, use `nagios4` instead.
> See also: `nagios2`, `nagios3`, `nagios4`.
> More information: <https://manned.org/nagios>.

- Start `nagios`:

`nagios /etc/nagios/nagios.cfg`

- Start `nagios` in daemon mode:

`nagios -d`

- Start `nagios`, print service check scheduling information to `stdout`, then shut down:

`nagios -s`

- Verify configuration file:

`nagios -v`
