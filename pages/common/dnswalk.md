# dnswalk

> DNS debugger.
> "Walks" across zones and validates database consistency and best practices.
> More information: <https://manned.org/dnswalk>.

- Debug a DNS pathway for a Full Qualified Domain Name (FQDN):

`dnswalk {{domain}}.`

- Descend sub-domains [r]ecursively:

`dnswalk -r {{domain}}.`

- Only perform a `dnswalk` if the zonme has been [m]odified since the last test:

`dnswalk -m {{domain}}.`

- Print [d]ebugging and status to `stderr` instead of `stdout`:

`dnswalk -d {{domain}}.`

- Suppress check for [i]nvalid characters in domain name:

`dnswalk -i {{domain}}.`

- Enable duplicate A record warning:

`dnswalk -a {{domain}}.`

- Enable "[F]ascist checking" to compare A record PTR name with the forward name and report mismatches:

`dnswalk -F {{domain}}.`

- Enable "[l]ame delegation" to test whether the listed host is returning authoritative answers:

`dnswalk -l {{domain.}}`
