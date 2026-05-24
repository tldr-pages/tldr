# lsmp

> Display Mach port names, rights, and peers for processes.
> More information: <https://keith.github.io/xcode-man-pages/lsmp.1.html>.

- Display Mach port usage and peer destinations for a specified PID (requires root privileges for detailed info):

`sudo lsmp -p {{pid}}`

- Display Mach port usage for [a]ll active tasks across the system:

`sudo lsmp -a`

- Increase information verbosity for kernel-object-based ports, including thread and special ports:

`sudo lsmp -p {{pid}} -v`

- Export Mach port information as a JSON file to a specific path:

`sudo lsmp -p {{pid}} -j {{path/to/output.json}}`
