# ionice

> get/set program io scheduling class and priority

- sets process with PID 89 as an idle io process

`ionice -c 3 -p 89`

- runs 'bash' as a best-effort program with highest priority

`ionice -c 2 -n 0 bash`

- prints the class and priority of the processes with PID 89

`ionice -p 89`
