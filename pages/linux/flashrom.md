# flashrom

> Read, write, verify and erase flash chips.
> More information: <https://man.archlinux.org/man/flashrom.8>.

- Probe the chip, ensuring the wiring is correct:

`flashrom -p {{programmer}}`

- Read flash and save it into file:

`flashrom -p {{programmer}} -r {{path/to/file}}`

- Write file into flash:

`flashrom -p {{programmer}} -w {{path/to/file}}`

- Erase flash:

`flashrom -p {{programmer}} -E`

- Probe the chip using RaspberryPi, an example:

`flashrom -p linux_spi:dev=/dev/spidev0.0`
