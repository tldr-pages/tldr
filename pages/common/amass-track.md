# amass track

> Track differences between enumerations of the same domain.
> More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>.

- Show the difference between the last two enumerations of the specified domain:

`amass track -dir {{path/to/database_directory}} -d {{domain_name}} -last 2`

- Show the difference between a certain point in time and the last enumeration:

`amass track -dir {{path/to/database_directory}} -d {{domain_name}} -since {{01/02 15:04:05 2006 MST}}`
