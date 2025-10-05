# expect

> Automate interactive command-line programs with scripted responses.
> Commonly used to automate SSH, FTP, or installer prompts.
> More information: <https://core.tcl-lang.org/expect/>.

- Run an Expect script file:

`expect {{path/to/script.exp}}`

- Run inline Expect commands:

`expect -c '{{commands}}'`

- Enable debug output to print interactions:

`expect -d {{path/to/script.exp}}`

- Start interactive debugging mode:

`expect -D 1 {{path/to/script.exp}}`

- Read and execute a script in buffered mode:

`expect -b {{path/to/script.exp}}`

- Automate a password prompt (example using `spawn`, `expect`, `send`, `interact`):

`expect -c 'spawn ssh {{user}}@{{host}}; expect "password:"; send "{{password}}\r"; interact'`

- Set a timeout within a script (common pattern):

`expect -c 'set timeout 5; spawn ./script; expect "prompt" { send "reply\r" }'`

- Display help or version information:

`expect --help`
