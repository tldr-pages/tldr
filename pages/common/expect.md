# expect

> Automate interactive command-line programs.
> More information: <https://core.tcl-lang.org/expect/index>.

- Run an expect script:

`expect {{script.exp}}`

- Run an expect script with a specific interpreter:

`expect -f {{script.exp}}`

- Pass arguments to an expect script:

`expect {{script.exp}} {{argument1}} {{argument2}}`

- Run an expect command directly from the command line:

`expect -c '{{spawn ssh user@host; expect "password:"; send "mypassword\r"; interact}}'`

- Run an expect script without closing after the last command:

`expect -i {{script.exp}}`
