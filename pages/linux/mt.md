# mt

> Control magnetic tape drive operation (commonly LTO tape).
> More information: <https://manned.org/mt>.

- Check tape status:

`mt -f {{/dev/[nst|st]N}} status`

- Rewind the tape to beginning:

`mt -f {{/dev/[nst|st]N}} rewind`

- Forward `<count>` files, then position tape on first block of next file:

`mt -f {{/dev/[nst|st]N}} fsf <count>`

- Rewind the tape, then position tape at beginning of `<count>` file:

`mt -f {{/dev/[nst|st]N}} asf <count>`

- Position tape at the end of valid data:

`mt -f {{/dev/[nst|st]N}} eod`

- Rewind the tape and unload/eject it:

`mt -f {{/dev/[nst|st]N}} eject`

- Write EOF (End-of-file) mark at the current position:

`mt -f {{/dev/[nst|st]N}} eof`
