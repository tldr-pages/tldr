# run_init

> Run init scripts in the proper SELinux context.
> Typically used to run system service scripts with correct SELinux domains.
> See also: `runcon`, `semanage`.
> More information: <https://manned.org/run_init>.

- Run a script in the init script context:

`sudo run_init {{path/to/script}}`

- Run a script with arguments:

`sudo run_init {{path/to/script}} {{start|stop|restart}}`

- Run a script and specify the init script context explicitly:

`sudo run_init {{[-t|--type]}} {{context_type}} {{path/to/script}}`

- Display the context that would be used without running the script:

`sudo run_init {{[-n|--dry-run]}} {{path/to/script}}`
