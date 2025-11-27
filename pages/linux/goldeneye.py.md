# goldeneye.py

> A HTTP DoS test tool.
> More information: <https://github.com/jseidl/GoldenEye#usage>.

- Test a specific website:

`{{path/to/}}goldeneye.py {{url}}`

- Test a specific website with 100 user agents and 200 concurrent sockets:

`{{path/to/}}goldeneye.py {{url}} {{[-u|--useragents]}} 100 {{[-s|--sockets]}} 200`

- Test a specific website without verifying the SSL certificate:

`{{path/to/}}goldeneye.py {{url}} --nosslcheck`

- Test a specific website in debug mode:

`{{path/to/}}goldeneye.py {{url}} --debug`

- Display help:

`{{path/to/}}goldeneye.py --help`
