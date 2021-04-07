# flashrom

> Read, write, verify and erase flash chips.
> More information: <https://man.archlinux.org/man/flashrom.8>.

- Probe the chip, ensuring the wiring is correct:

`flashrom --programmer {{programmer}}`

- Read flash and save it into file:

`flashrom -p {{programmer}} --read {{path/to/file}}`

- Write file into flash:

`flashrom -p {{programmer}} --write {{path/to/file}}`

- Verify flash against file:

`flashrom -p {{programmer}} --verify {{path/to/file}}`

- Probe the chip using RaspberryPi, an example:

`flashrom -p linux_spi:dev=/dev/spidev0.0`
