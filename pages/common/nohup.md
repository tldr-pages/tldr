# nohup

> Allows for a process to live when the terminal gets killed.
> More information: <https://www.gnu.org/software/coreutils/nohup>.

- Run a process that can live beyond the terminal:

`nohup {{command}} {{command_options}}`

- Launch nohup in background mode:

`nohup {{command}} {{command_options}} &`

- Run a shell script that can live beyond the terminal:

`nohup {{path/to/shell/script}} &`

- Run a process and choose a path for nohup.out log file:

`nohup {{command}} {{command_options}} > {{path/to/custom.out}} &`
