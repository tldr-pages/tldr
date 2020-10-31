# theHarvester

> A tool designed to be used in the early stages of a penetration test.
> More information: <https://github.com/laramies/theHarvester>.

- Gather information on a domain using Google:

`theHarvester --domain {{domain_name}} --source google`

- Gather information on a domain using multiple sources:

`theHarvester --domain {{domain_name}} --source google,bing,crtsh`

- Change the limit of results to work with:

`theHarvester --domain {{domain_name}} --source google --limit 200`

- Save the output to an xml and html file:

`theHarvester --domain {{domain_name}} --source google --file {{output_file}}`

- Output all available options:

`theHarvester --help`
