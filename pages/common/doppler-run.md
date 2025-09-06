# doppler run

> Run a command with Doppler secrets injected into the environment.
> More information: <https://docs.doppler.com/docs/cli#run-a-command-with-secrets-populated-in-environment>.

- Run a command:

`doppler run --command {{command}}`

- Run multiple commands:

`doppler run --command {{command1 && command2}}`

- Run a script:

`doppler run {{path/to/command.sh}}`

- Run command with specified project and config:

`doppler run -p {{project_name}} -c {{config_name}} -- {{command}}`

- Automatically restart process when secrets change:

`doppler run --watch {{command}}`
