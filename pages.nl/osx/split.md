# split

> Split een bestand in stukken.
> Meer informatie: <https://keith.github.io/xcode-man-pages/split.1.html>.

- Split een bestand, elk deel heeft 10 regels (behalve het laatste deel):

`split -l 10 {{pad/naar/bestand}}`

- Split een bestand op een reguliere expressie. De overeenkomende regel zal de eerste regel van het volgende uitvoerbestand zijn:

`split -p {{cat|^[dh]og}} {{pad/naar/bestand}}`

- Split een bestand met 512 bytes in elk deel (behalve het laatste deel; gebruik 512k voor kilobytes en 512m voor megabytes):

`split -b 512 {{pad/naar/bestand}}`

- Split een bestand in 5 bestanden. Het bestand wordt zo gesplitst dat elk deel dezelfde grootte heeft (behalve het laatste deel):

`split -n 5 {{pad/naar/bestand}}`
