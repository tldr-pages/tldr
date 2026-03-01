# imp

> A helper to use native systemd support under WSL (Windows Subsystem for Linux).
> To run these from Windows rather than an already-running distribution, precede them with `wsl`.
> More information: <https://github.com/arkane-systems/bottle-imp>.

- Initialize the helper functions and keep WSL running until explicit shutdown (run once, at start):

`imp {{[-i|--initialize]}}`

- Run a shell inside a systemd user session:

`imp {{[-s|--shell]}}`

- Run a specified command inside a systemd user session (preserves working directory):

`imp {{[-c|--command]}} {{command}}`

- Shut down systemd and the WSL instance:

`imp {{[-u|--shutdown]}}`
