# abrt-cli

> Automatic Bug Reporting Tool for Fedora-based systems.
> Used to detect, analyze, and report application crashes.
> More information: <https://abrt.readthedocs.io/>.

- List detected problems:

`abrt-cli list`

- Show details of a specific problem:

`abrt-cli info {{problem_id}}`

- Remove a crash report:

`abrt-cli remove {{problem_id}}`

- Report a problem to the configured bug tracker (e.g., Bugzilla):

`abrt-cli report {{problem_id}}`

- Watch for new crashes in real time (requires the `abrt-watch-log` service):

`abrt-watch-log -f {{/path/to/logfile}}`

- Generate a report for debugging manually:

`abrt-cli report --analyze {{problem_id}}`
