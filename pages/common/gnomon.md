# gnomon

> Utility to annotate console logging statements with timestamps and find slow processes.
> More information: <https://github.com/paypal/gnomon#options>.

- Use UNIX (or DOS) pipes to pipe `stdout` of any command through gnomon:

`{{npm test}} | gnomon`

- Show number of seconds since the start of the process:

`{{npm test}} | gnomon {{[-t|--type]}} elapsed-total`

- Show an absolute timestamp in UTC:

`{{npm test}} | gnomon {{[-t|--type]}} absolute`

- Use a high threshold of 0.5 seconds, exceeding which the timestamp will be colored bright red:

`{{npm test}} | gnomon {{[-h|--high]}} 0.5`

- Use a medium threshold of 0.2 seconds, exceeding which the timestamp will be colored bright yellow:

`{{npm test}} | gnomon {{[-m|--medium]}} {{0.2}}`
