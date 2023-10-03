# crystal

> Tool for managing Crystal source code.
> More information: <https://crystal-lang.org/reference/using_the_compiler>.

- Run a Crystal file:

`crystal {{path/to/file.cr}}`

- Compile a file and all dependencies to a single executable:

`crystal build {{path/to/file.cr}}`

- Read Crystal source code from the command line or `stdin`, and execute it:

`crystal eval '{{code}}'`

- Generate API documentation from inline docstrings in Crystal files:

`crystal docs`

- Compile and run a Crystal specification suite:

`crystal spec`

- Start a local interactive server for testing the language:

`crystal play`

- Create a project directory for a Crystal application:

`crystal init app {{application_name}}`

- Display all help options:

`crystal help`
