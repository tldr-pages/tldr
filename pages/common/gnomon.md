# gnomon

> Utility to annotate console logging statements with timestamps and find slow processes.
> More information: <https://github.com/paypal/gnomon>.

- Use UNIX (or DOS) pipes to pipe the stdout of any command through gnomon:

`{{npm test}} | gnomon`

- Show number of seconds since the start of the process:

`{{npm test}} | gnomon --type=elapsed-total`

- Show an absolute timestamp in UTC:

`{{npm test}} | gnomon --type=absolute`

- Set a high threshold of 0.5 seconds for the elapsed time; exceeding which the timestamp will be colored bright red:

`{{npm test}} | gnomon --high {{0.5}}`

- Set a medium threshold of 0.2 seconds (Timestamp will be colored bright yellow):

`{{npm test}} | gnomon --medium {{0.2}}`
