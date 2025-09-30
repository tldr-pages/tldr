# abrt-cli

> Automatic Bug Reporting Tool for Fedora-based systems.
> Used to detect, analyze, and report application crashes.
> More information: <https://abrt.readthedocs.io/en/latest/usage.html>.

- List detected problems:

`abrt-cli list`

- Show details of a specific problem:

`abrt-cli info {{problem_id}}`

- Remove a crash report:

`abrt-cli remove {{problem_id}}`

- Report a problem to the configured bug tracker (e.g. Bugzilla):

`abrt-cli report {{problem_id}}`

- Monitor a log file and trigger a program when a match is found:

`abrt-watch-log -F {{error_string}} {{/var/log/myapp.log}} {{notify-send "Crash detected"}}`

- Generate a report for debugging manually:

`abrt-cli report {{[-a|--analyze]}} {{problem_id}}`
