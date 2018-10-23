# gnomon 

> Utility to annotate console logging statements with timestamps and find slow processes.

- Use UNIX (or DOS) pipes to pipe the stdout of any command through gnomon:

`{{npm test}} | gnomon`

- Show number of seconds since the start of the process:

`{{npm test}} | gnomon --type=elapsed-total`

- Show an absolute timestamp in UTC:

`{{npm test}} | gnomon --type=absolute`

- Format the absolute timestamp, using PHP date format strings:

`{{npm test}} | gnomon --type=absolute --format "H:i:s.u 0"`

- High threshold. If the elapsed time for a line is equal to or higher than this value in seconds, then the timestamp will be colored bright red:

`{{npm test}} | gnomon --high 0.5`

- Medium threshold. If the elapsed time for a line is equal to or higher than this value in seconds, then the timestamp will be colored bright yellow:

`{{npm test}} | gnomon --medium 0.5`
