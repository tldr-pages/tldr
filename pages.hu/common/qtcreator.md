# qtcreator

> Cross-platform IDE Qt alkalmazásokhoz. További információ: <https://doc.qt.io/qtcreator/creator-cli.html>.

- Indítsa el a Qt Creatort:

`qtcreator`

- A Qt Creator elindítása és a legutóbbi munkamenet visszaállítása:

`qtcreator -lastsession`

- Indítsa el a Qt Creatort, de ne töltse be a megadott plugint:

`qtcreator -noload {{plugin}}`

- Indítsa el a Qt Creatort, de ne töltsön be egyetlen bővítményt sem:

`qtcreator -noload {{all}}`

- A Qt Creator elindítása prezentációs módban, billentyűparancsok felugró ablakokkal:

`qtcreator -presentationMode`

- A Qt Creator indítása és a diff megjelenítése egy adott commitból:

`qtcreator -git-show {{commit}}`
