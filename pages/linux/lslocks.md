# lslocks

> List all local system locks.

- List all local system locks:

`lslocks`

- List locks with defined column headers:

`lslocks -o PID,COMMAND,PATH`

- List locks raw output (no columns), and no column headers:

`lslocks -r -n`

- Populate a csv file with the information from above command:

`lslocks -r -n | tr ' ' ',' > {{filename.csv}}`
