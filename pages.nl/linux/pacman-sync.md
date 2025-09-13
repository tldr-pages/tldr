# pacman --sync

> Hulpprogramma voor het beheren van pakketten op Arch Linux.
> Zie ook: `pacman`.
> Meer informatie: <https://manned.org/pacman.8>.

- Installeer een nieuw pakket:

`sudo pacman -S {{pakket}}`

- [S]ynchroniseer en ververs ([y]) de pakketdatabase en voer een sys[u]pgrade uit (voeg `--downloadonly` toe om alleen de pakketten te downloaden en niet te upgraden):

`sudo pacman -Syu`

- Update en [u]pgrade alle pakketten en installeer een nieuw pakket zonder bevestiging:

`sudo pacman -Syu --noconfirm {{pakket}}`

- Doorzoek ([s]) de pakketdatabase met een reguliere expressie of zoekwoord:

`pacman -Ss "{{zoekterm}}"`

- Toon [i]nformatie over een pakket:

`pacman -Si {{pakket}}`

- Overschrijf conflicterende bestanden tijdens een pakketupdate:

`sudo pacman -Syu --overwrite {{pad/naar/bestand}}`

- Verwijder niet-geïnstalleerde pakketten en ongebruikte repositories uit de cache (gebruik de vlag `Sc` om [c]ache volledig schoon te maken):

`sudo pacman -Sc`

- Specificeer de pakketversie die geïnstalleerd dient te worden:

`sudo pacman -S {{pakket}}={{versie}}`
