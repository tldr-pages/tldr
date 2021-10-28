# mt

> Control magnetic tape drive operation (commonly LTO tape)<br>
> More information: <https://linux.die.net/man/1/mt>.

- Check tape status:

`mt -f <device> status`

- Rewind the tape to beginning:

`mt -f <device> rewind`

- Forward `<count>` files, then position tape on first block of next file:

`mt -f <device> fsf <count>`

- Rewind the tape, then position tape at beginning of `<count>` file:

`mt -f <device> asf <count>`

- Position tape at the end of valid data:

`mt -f <device> eod`

- Rewind the tape and unload/eject it:

`mt -f <device> eject`

- Write EOF (End-of-file) mark at current position:

`mt -f <device> eof`
