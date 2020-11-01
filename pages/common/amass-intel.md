# amass intel

> Collect open source intel on an organisation like root domains and ASNs.
> More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Find root domains in an IP address range:

`amass intel -addr {{192.168.0.1-254}}`

- Use active recon methods:

`amass intel -active -addr {{192.168.0.1-254}}`

- Find root domains related to a domain:

`amass intel -whois -d {{domain_name}}`

- Find ASNs belonging to an organisation:

`amass intel -org {{organisation_name}}`

- Find root domains belonging to a given Autonomous System Number:

`amass intel -asn {{asn}}`

- Save results to a text file:

`amass intel -o {{output_file}} -whois -d {{domain_name}}`
