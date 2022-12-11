# goldeneye.py

> A HTTP DoS test tool.
> More information: <https://github.com/jseidl/GoldenEye>.

- Test a specific website:

`./goldeneye.py {{url}}`

- Test a specific website with 100 user agents and 200 concurrent sockets:

`./goldeneye.py {{url}} --useragents 100 --sockets 200`

- Test a specific website without verifying the SSL certificate:

`./goldeneye.py {{url}} --nosslcheck`

- Test a specific website in debug mode:

`./goldeneye.py {{url}} --debug`

- Display help:

`./goldeneye.py --help`
