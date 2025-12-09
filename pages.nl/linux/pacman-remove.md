# pacman --remove

> Hulpprogramma voor het beheren van pakketten op Arch Linux.
> Zie ook: `pacman`.
> Meer informatie: <https://manned.org/pacman.8>.

- Verwijde[R] een pakket en zijn afhankelijkheden recur[s]ief:

`sudo pacman -Rs {{pakket}}`

- Verwijde[R] een pakket en zijn afhankelijkheden. Maak ook gee[n] back-ups van configuratiebestanden:

`sudo pacman -Rsn {{pakket}}`

- Verwijde[R] een pakket zonder bevestigingsprompt:

`sudo pacman -R --noconfirm {{pakket}}`

- Verwijde[R] weespakketten (geïnstalleerd als [d]ependencies maar [n]iet vereist door een ander pakket):

`sudo pacman -Rsn $(pacman -Qdtq)`

- Verwijde[R] een pakket en [c]ascadeer dat naar alle pakketten die ervan afhankelijk zijn:

`sudo pacman -Rc {{pakket}}`

- Toon en [p]rint pakketten die beïnvloed zouden worden (verwijdert [R] geen pakketten):

`pacman -Rp {{pakket}}`

- Toon [h]ulp:

`pacman -Rh`
