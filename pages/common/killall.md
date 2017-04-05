# killall

> Send kill signal to all instances of a process by name.
> All signals except SIGKILL and SIGSTOP can be intercepted by the process, allowing a clean exit.

- Terminate a process using the default SIGTERM (terminate) signal:

`killall {{process_name}}`

- List available signal names (to be used without the 'SIG' prefix):

`killall -l`

- Interactively ask for confirmation before termination:

`killall -i {{process_name}}`

- Terminate a process using the SIGING (interrupt) signal, which is the same signal sent by pressing `Ctrl+C`:

`killall -INT {{process_name}}`

- Immediately kill a process (signal cannot be intercepted so it's not a clean exit):

`killall -KILL {{process_name}}`
