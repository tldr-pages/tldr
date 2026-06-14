# svcs

> Managing and querying the status of system services.
> More information: <https://docs.oracle.com/cd/E86824_01/html/E54763/svcs-1.html>.

- List all running services:

`svcs`

- List all defined service:

`svcs -a`

- Show service status:

`svcs {{service_fmri}}`

- Show service detailed status:

`svcs -l {{service_fmri}}`

- Show failed or not running service with description:

`svcs -x`

- Show service log file path:

`svcs -L {{service_fmri}}`

- Show service last logs:

`svcs -xL {{service_fmri}}`

- Show service verbose logs:

`svcs -xv {{service_fmri}}`

- Show the complete log:

`svcs -vL {{service_fmri}}`

- Show PID of service processes:

`svcs -p {{service_fmri}}`

- List service dependencies:

`svcs -d {{service_fmri}}`

- List service dependents:

`svcs -D {{service_fmri}}`
