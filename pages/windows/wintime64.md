# WinTime64

> Measure a 64-bit program's execution time and memory usage.
> Use `WinTime32` instead for 32-bit programs.
> More information: <https://github.com/cbielow/wintime>.

- Measure a 64-bit program's execution time and memory usage:

`WinTime64 -- "{{path\to\program.exe}}"`

- Display the command and its arguments along with resource usage:

`WinTime64 --verbose -- "{{path\to\program.exe}}" {{arguments}}`

- Write resource usage to a file, overwriting any existing contents:

`WinTime64 --output "{{path\to\file}}" -- "{{path\to\program.exe}}"`

- Append resource usage to a file:

`WinTime64 --append --output "{{path\to\file}}" -- "{{path\to\program.exe}}"`

- Display help:

`WinTime64 --help`

- Display version:

`WinTime64 --version`
