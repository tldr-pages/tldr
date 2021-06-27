# vnstati

> PNG image output support for vnStat.
> More information: <https://linux.die.net/man/1/vnstati>.

- Output summary of the last 2 days/months and all time:

`vnstati -s -i {{network_interface}} -o {{output}}.png`

- Output all time top 10 traffic days:

`vnstati -t -i {{network_interface}} -o {{output}}.png`

- Output traffic statistics on a monthly basis for the last 12 months:

`vnstati -m -i {{network_interface}} -o {{output}}.png`

- Output traffic statistics on a hourly basis for the last 24 hours:

`vnstati -h -i {{network_interface}} -o {{output}}.png`
