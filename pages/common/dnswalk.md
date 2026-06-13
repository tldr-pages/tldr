# dnswalk

> DNS debugger.
> "Walk" across zones and validate database consistency and best practices.
> More information: <https://manned.org/dnswalk>.

- Debug a DNS pathway for a Fully Qualified Domain Name (FQDN):

`dnswalk {{domain}}.`

- Process sub-domains [r]ecursively:

`dnswalk -r {{domain}}.`

- Only perform a `dnswalk` if the zone has been [m]odified since the last run:

`dnswalk -m {{domain}}.`

- Print [d]ebugging and status information to `stderr` instead of `stdout`:

`dnswalk -d {{domain}}.`

- Suppress the check for [i]nvalid characters in the domain name:

`dnswalk -i {{domain}}.`

- Enable duplicate A record warnings:

`dnswalk -a {{domain}}.`

- Enable "[F]ascist checking" to compare the A record PTR name with the forward name and report mismatches:

`dnswalk -F {{domain}}.`

- Enable "[l]ame delegation" to test whether the listed host is returning authoritative answers:

`dnswalk -l {{domain}}.`
