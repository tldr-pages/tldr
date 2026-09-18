# faketime

> Fake the system time for a command.
> More information: <https://manned.org/faketime>.

- Fake the time to this evening, before printing the result of `date`:

`faketime '{{today 23:30}}' {{date}}`

- Open a new Bash shell, which uses yesterday as the current date:

`faketime '{{yesterday}}' {{bash}}`

- Simulate how a program would act next Friday night:

`faketime '{{next Friday 1 am}}' {{path/to/program}}`

- Run a program on a specific date and time:

`faketime '{{2020-01-01 12:00:00}}' {{program}}`
