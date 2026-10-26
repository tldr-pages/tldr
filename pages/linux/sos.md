# sos

> A unified tool for collecting system logs and other debug information.
> Used by system administrators and support representatives to assist in troubleshooting.
> More information: <https://github.com/sosreport/sos>.

- Generate an archive of system information and configuration:

`sudo sos report`

- Generate a report tagged with a support case ID:

`sudo sos report --case-id {{case_id}}`

- Generate a report and upload it to the distribution support target:

`sudo sos report --upload`

- List all available plugins and their options:

`sudo sos report {{[-l|--list-plugins]}}`

- Collect complete logs without size restriction:

`sudo sos report --all-logs`

- Generate a report non-interactively without prompts:

`sudo sos report --batch`

- Add a custom label to the generated archive name:

`sudo sos report --label {{label}}`

- Save the generated archive to a specific directory:

`sudo sos report --tmp-dir {{path/to/directory}}`
