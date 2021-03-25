# pkill

> Signal process by name.
> Mostly used for stopping processes.
> More information: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>.

- Kill all processes which match:

`pkill -9 "{{process_name}}"`

- Kill all processes which match their full command instead of just the process name:

`pkill -9 --full "{{command_name}}"`

- Send SIGUSR1 signal to processes which match:

`pkill -USR1 "{{process_name}}"`

- Kill the main `firefox` process to close the browser:

`pkill --oldest "{{firefox}}"`
