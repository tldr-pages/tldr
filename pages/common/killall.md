# killall

> Send kill signal to all instances of a process by name (must be exact name).
> All signals except SIGKILL and SIGSTOP can be intercepted by the process, allowing a clean exit.

- Terminate a process using the default SIGTERM (terminate) signal:

`killall {{exact_process_name}}`

- List available signal names (to be used without the 'SIG' prefix):

`killall --list`

- Interactively ask for confirmation before termination:

`killall -i {{exact_process_name}}`

- Terminate a process using the SIGING (interrupt) signal, which is the same signal sent by pressing `Ctrl+C`:

`killall -INT {{exact_process_name}}`

- Immediately kill a process (signal cannot be intercepted so it's not a clean exit):

`killall -KILL {{exact_process_name}}`
