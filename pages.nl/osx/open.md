# open

> Open bestanden, mappen en applicaties.
> Meer informatie: <https://keith.github.io/xcode-man-pages/open.1.html>.

- Open een bestand met de bijbehorende applicatie:

`open {{bestand.ext}}`

- Start een grafische macOS-[a]pplicatie:

`open -a "{{Applicatie}}"`

- Start een grafische macOS-app op basis van de [b]undle-identificator (raadpleeg `osascript` voor een eenvoudige manier om deze te verkrijgen):

`open -b {{com.domein.applicatie}}`

- Open de huidige map in Finder:

`open .`

- Toon ([R]) een bestand in Finder:

`open -R {{pad/naar/bestand}}`

- Open alle bestanden met een bepaalde extensie in de huidige map met de bijbehorende applicatie:

`open {{*.ext}}`

- Open een [n]ieuw exemplaar van een applicatie gespecificeerd via de [b]undle-identificator:

`open -n -b {{com.domein.applicatie}}`
