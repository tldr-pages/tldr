# tee

> Lees van `stdin` en schrijf naar `stdout` en bestanden (of commando's).
> Meer informatie: <https://www.gnu.org/software/coreutils/tee>.

- Kopieer `stdin` naar elk bestand en ook naar `stdout`:

`echo "voorbeeld" | tee {{pad/naar/bestand}}`

- Voeg toe aan de opgegeven bestanden, overschrijf niet:

`echo "voorbeeld" | tee -a {{pad/naar/bestand}}`

- Toon `stdin` naar de terminal en leid het ook door naar een ander programma voor verdere verwerking:

`echo "voorbeeld" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Maak een directory genaamd "voorbeeld", tel het aantal tekens in "voorbeeld" en schrijf "voorbeeld" naar de terminal:

`echo "voorbeeld" | tee >(xargs mkdir) >(wc -c)`
