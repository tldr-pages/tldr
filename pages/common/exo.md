# exo

> The official CLI tool for Exoscale services.
> Some subcommands such as `exo compute` have their own usage documentation.
> More information: <https://community.exoscale.com/community/tools/exoscale-command-line-interfaces>.

- Configure the exo command-line:

`exo config`

- Generate the exo autocompletion script for a specified shell:

`exo completion {{zsh}}`

- List all of the available zones and output them as json:

`exo zone {{[-O|--output-format]}} {{json}}`

- Quietly create a Compute instance in a specific zone (disables the non-essential command output):

`exo compute instance create {{instance_name}} --zone {{zone}} {{[-Q|--quiet]}}`

- List just the name of all of the buckets in the Organization:

`exo storage list {{[-O|--output-template]}} '\{\{ .Name \}\}`

- Display help for a command:

`exo {{iam}} {{[-h|--help]}}`
