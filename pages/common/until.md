# until

> Simple shell loop that repeats until it receives zero as return value.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-until>.

- Execute a command until it succeeds:

`until {{command}}; do :; done`

- Wait for a systemd service to be active:

`until systemctl is-active {{[-q|--quiet]}} {{nginx}}; do {{echo "Waiting..."}}; sleep 1; done; {{echo "Launched!"}}`
