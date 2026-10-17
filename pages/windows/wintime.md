# wintime

> Measure the execution time and peak memory usage of a Windows process.
> More information: <https://github.com/cbielow/wintime>.

- Measure a program's wall, user, and kernel time, as well as its peak memory usage:

`WinTime64.exe "{{path\to\program.exe}}"`

- Run a program with arguments, ensuring that they are passed to the program rather than interpreted by WinTime:

`WinTime64.exe -- "{{path\to\program.exe}}" {{argument1 argument2 ...}}`

- Print the command and arguments before measuring the program:

`WinTime64.exe --verbose "{{path\to\program.exe}}"`

- Write the measurement results to a file instead of `stderr`:

`WinTime64.exe --output "{{path\to\log.txt}}" "{{path\to\program.exe}}"`

- Append the measurement results to an existing file:

`WinTime64.exe --append --output "{{path\to\log.txt}}" "{{path\to\program.exe}}"`

- Display help:

`WinTime64.exe --help`

- Display version information:

`WinTime64.exe --version`
