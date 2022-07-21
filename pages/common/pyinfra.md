# pyinfra

> Automates infrastructure at a large scale.
> More information: <https://docs.pyinfra.com>.

- Execute a command over ssh:

`pyinfra {{target_ip_address}} exec -- {{command_name_and_arguments}}`

- Execute contents of a deploy file on a list of targets:

`pyinfra {{path/to/inventory.py}} {{path/to/deploy.py}}`

- Execute commands on your local machine:

`pyinfra @local exec -- {{command_name_and_arguemnts}}`

or

`pyinfra @local {{path/to/deploy.py}}`

- Execute commands over Docker:

`pyinfra @docker/{{container}} exec -- {{command_name_and_arguemnts}}`

or

`pyinfra @docker/{{container}} {{path/to/deploy.py}}`
