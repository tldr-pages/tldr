# mt

> Control magnetic tape drive operation (commonly LTO tape).
> More information: <https://manned.org/mt>.

- Check the status of a tape drive:

`mt -f {{/dev/[nst|st]N}} status`

- Rewind the tape to beginning:

`mt -f {{/dev/[nst|st]N}} rewind`

- Move forward a given files, then position the tape on first block of next file:

`mt -f {{/dev/nstX}} fsf {{count}}`

- Rewind the tape, then position the tape at beginning of the given file:

`mt -f {{/dev/nstX}} asf {{count}}`

- Position the tape at the end of valid data:

`mt -f {{/dev/[nst|st]N}} eod`

- Rewind the tape and unload/eject it:

`mt -f {{/dev/[nst|st]N}} eject`

- Write EOF (End-of-file) mark at the current position:

`mt -f {{/dev/[nst|st]N}} eof`
