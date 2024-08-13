# sum

> Bereken checksums en het aantal blokken voor een bestand.
> Een voorloper van de modernere `cksum`.
> Meer informatie: <https://www.gnu.org/software/coreutils/sum>.

- Bereken een checksum met een BSD-compatibel algoritme en 1024-byte blokken:

`sum {{pad/naar/bestand}}`

- Bereken een checksum met een System V-compatibel algoritme en 512-byte blokken:

`sum --sysv {{pad/naar/bestand}}`
