# faketime

> Fake the system time for a given command.
> More information: <https://manpages.ubuntu.com/manpages/trusty/man1/faketime.1.html>.

- Fake the time to this evening, before printing the result of `date`:

`faketime '{{today 23:30}}' {{date}}`

- Open a new `bash` shell, which uses yesterday as the current date:

`faketime '{{yesterday}}' {{bash}}`

- Simulate how any program would act next friday night:

`faketime '{{next Friday 1 am}}' {{path/to/any/program}}`
