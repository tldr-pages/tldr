# gnomon 

> Utility to annotate console logging statements with timestamps and find slow processes.

- Use UNIX (or DOS) pipes to pipe the stdout of any command through gnomon:

`npm test | gnomon`

- Use command-line options to adjust gnomon's behavior for any command:

`{{any command}} | gnomon --type=elapsed-total --high=8.0`
