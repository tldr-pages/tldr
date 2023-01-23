# forever

> Szerveroldali JavaScript alkalmazás, amely biztosítja, hogy a Node.js alkalmazások korlátlan ideig fussanak (kilépés után újraindul). További információ: <https://github.com/foreversd/forever>.

- Egy fájl örökké tartó futtatásának elindítása (démonként):

`forever {{script}}`

- A futó "örökké" folyamatok listázása (az "örökké" folyamatok azonosítóival és egyéb részleteivel együtt):

`forever list`

- Egy futó "örökké" folyamat leállítása:

`forever stop {{ID|pid|script}}`
