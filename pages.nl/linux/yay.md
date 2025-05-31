# yay

> Yet Another Yogurt: bouw en installeer pakketten van de Arch User Repository.
> Bekijk ook: `pacman`.
> Meer informatie: <https://github.com/Jguer/yay>.

- Zoek en installeer interactief pakketten van de bronnen en AUR:

`yay {{pakket_naam|zoekpatroon}}`

- Synchroniseer en update alle pakketten van de bronnen en AUR:

`yay`

- Installeer een nieuw pakket van de bronnen en AUR en vraag niet om transacties te bevestigen:

`yay -S {{pakket}} --noconfirm`

- Verwijder een geïnstalleerd pakket en de bijbehorende afhankelijkheden en configuratiebestanden:

`yay -Rns {{pakket}}`

- Doorzoek de pakketdatabase voor een sleutelwoord van de bronnen en AUR:

`yay -Ss {{sleutelwoord}}`

- Verwijder weespakketten (geïnstalleerd als afhankelijkheden maar niet daadwerkelijk vereist door een ander pakket):

`yay -Yc`

- Leeg de `pacman` en `yay` caches (oude pakketversies worden bewaard voor rollback- en downgrade-doeleinden):

`yay -Scc`

- Toon statistieken van geïnstalleerde pakketten en systeemstatus:

`yay -Ps`
