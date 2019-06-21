# phpspec

> A SpecBDD testing framework for PHP.
> More information: <https://phpspec.net>.

- Describe a new class specification:

`phpspec describe {{class_name}}`

- Run all specficiations in the "spec" directory:

`phpspec run`

- Run a specific specification:

`phpspec run {{path/to/class_specification_file}}`

- Run specifications using a specific configuration file:

`phpspec run -c {{path/to/configuration_file}}`

- Run specifications using a specific bootstrap file:

`phpspec run -b {{path/to/bootstrap_file}}`

- Disable code generation prompts:

`phpspec run --no-code-generation`

- Enable fake return values:

`phpspec run --fake`
