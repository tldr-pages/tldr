# urpmq

> Query information about packages and media in Mageia.
> See also: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpme`.
> More information: <https://man.linuxreviews.org/man8/urpmq.8.html>.

- Display information about an installable package:

`urpmq -i {{package}}`

- Display direct dependencies of a package:

`urpmq --requires {{package}}`

- Display direct and indirect dependencies of a package:

`urpmq {{[-d|--requires-recursive]}} {{package}}`

- List the not installed packages needed for an RPM file with their sources:

`sudo urpmq {{[-d|--requires-recursive]}} -m --sources {{path/to/file.rpm}}`

- List all configured media with their URLs, including inactive media:

`urpmq --list-media --list-url`

- Search for a package printing [g]roup, version and [r]elease:

`urpmq -g -r {{[-y|--fuzzy]}} {{keyword}}`

- Search for a package with using its exact name:

`urpmq -g -r {{package}}`
