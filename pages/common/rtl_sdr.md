# rtl_sdr

> I/Q recorder for RTL-SDR receivers.
> More information: <https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>.

- Save RAW data from frequency specified in Hz in file:

`rtl_sdr -f {{100000000}} {{path/to/file}}`

- Pipe data to another program:

`rtl_sdr -f {{100000000}} - | {{aplay}}`

- Read specific number of samples:

`rtl_sdr -f {{100000000}} -n {{20}} -`

- Specify sample rate in Hz (ranges 225001-300000 and 900001-3200000):

`rtl_sdr -f {{100000000}} -s {{2400000}} -`

- Specify device by index:

`rtl_sdr -f {{100000000}} -d {{0}} -`

- Specify gain:

`rtl_sdr -f {{100000000}} -g {{20}} -`

- Specify output block size:

`rtl_sdr -f {{100000000}} -b {{9999999}} -`

- Use synchronous output:

`rtl_sdr -f {{100000000}} -S -`
