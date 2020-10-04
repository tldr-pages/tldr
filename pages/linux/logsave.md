# logsave

> Save the output of a command in a logfile.
> More information: <https://linux.die.net/man/8/logsave>.

- Execute command with specified argument(s) and save its output to logfile:

`logsave {{logfile}} {{command}}`

- Take input from standard input and save it in logfile:

`logsave {{logfile}} -`

- Append the output to logfile, instead of replacing its current contents:

`logsave -a {{logfile}} {{command}}`

- Show verbose output:

`logsave -v {{logfile}} {{command}}`
