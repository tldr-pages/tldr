# genie

> Set up and use a "bottle" namespace to run systemd under WSL (Windows Subsystem for Linux).
> To run these from Windows rather than an already-running distribution, precede them with `wsl`.
> More information: <https://github.com/arkane-systems/genie>.

- Initialize the bottle (run once, at start):

`genie -i`

- Run a login shell inside the bottle:

`genie -s`

- Run a specified command inside the bottle:

`genie -c {{command}}`
