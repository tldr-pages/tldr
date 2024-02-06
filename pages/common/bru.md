# bru

> CLI for Bruno, an Opensource IDE for exploring and testing APIs.
> More information: <https://docs.usebruno.com/cli/overview.html>.

- Run all request files from the current directory:

`bru run`

- Run a single request from the current directory by specifying its filename:

`bru run {{file.bru}}`

- Run requests using an environment:

`bru run --env {{environment_name}}`

- Run requests using an environment with a variable:

`bru run --env {{environment_name}} --env-var {{variable_name}}={{variable_value}}`

- Run request and collect the results in an output file:

`bru run --output {{path/to/output.json}}`

- Display help:

`bru run --help`
