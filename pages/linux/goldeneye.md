# goldeneye

> A http DoS test tool.
> More information: <https://github.com/jseidl/GoldenEye>.

- Test a specific website:

`./goldeneye.py {{website_url}}"`

- Test a specific website with 100 user agents and 200 concurrent sockets:

`./goldeneye.py {{website_url}} -u {{100}} -s {{200}}"`

- Test a specific website without verifying ssl certficate:

`./goldeneye.py {{website_url}} -n"`

- Test a specific website in debug mode:

`./goldeneye.py {{website_url}} -d"`

- Display help:

`./goldeneye.py -h"`
