# toybox

> Multipurpose command-line tool that provides many standard Unix utilities.
> Commonly used in Android and embedded Linux systems.
> More information: <https://landley.net/toybox/>.

- List all available Toybox commands:

`toybox`

- Display help information for a specific command:

`toybox {{command}} --help`

- Show version information:

`toybox --version`

- Run a Toybox command explicitly (useful if another command with the same name exists in `$PATH`):

`toybox {{command}} {{arguments}}`

- Example: list files in the current directory using Toybox:

`toybox ls`

- Remove a file:

`toybox rm {{path/to/file}}`
