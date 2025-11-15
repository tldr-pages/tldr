# nagios3

> Legacy host/service/networking monitoring program.
> Largely deprecated by `nagios4`.
> See also: `nagios`, `nagios2`, `nagios4`.
> More information: <https://manned.org/nagios>.

- Start `nagios3`:

`nagios3 /etc/nagios3/nagios.cfg`

- Start `nagios3` in daemon mode:

`nagios3 -d`

- Start `nagios3`, print service check scheduling information to `stdout`, then shutdown:

`nagios3 -s`

- Verify configuration file:

`nagios3 -v`
