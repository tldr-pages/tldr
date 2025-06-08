# split

> Split een bestand in stukken.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>.

- Split een bestand, elk deel heeft 10 regels (behalve het laatste deel):

`split {{[-l|--lines]}} 10 {{pad/naar/bestand}}`

- Split een bestand in 5 bestanden. Het bestand wordt zo gesplitst dat elk deel dezelfde grootte heeft (behalve het laatste deel):

`split {{[-n|--number]}} 5 {{pad/naar/bestand}}`

- Split een bestand met 512 bytes in elk deel (behalve het laatste deel; gebruik 512k voor kilobytes en 512m voor megabytes):

`split {{[-b|--bytes]}} 512 {{pad/naar/bestand}}`

- Splits een bestand met maximaal 512 bytes in elk deel zonder regels te breken:

`split {{[-C|--line-bytes]}} 512 {{pad/naar/bestand}}`
