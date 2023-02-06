# tree

> Az aktuális könyvtár tartalmának faként való megjelenítése. További információ: <http://mama.indstate.edu/users/ice/tree/>.

- Fájlok és könyvtárak kiírása 'num' mélységi szintig (ahol 1 az aktuális könyvtárat jelenti):

`tree -L {{num}}`

- Csak könyvtárak nyomtatása:

`tree -d`

- Nyomtassa ki a rejtett fájlokat is, bekapcsolt színezéssel:

`tree -a -C`

- Nyomtassa ki a fát behúzási sorok nélkül, helyette a teljes elérési utat mutatva (használja a `-N` címet a nem nyomtatható karakterek elkerülése érdekében):

`tree -i -f`

- Nyomtassa ki az egyes fájlok méretét és az egyes könyvtárak összesített méretét, ember által olvasható formátumban:

`tree -s -h --du`

- A fahierarchián belüli fájlok kinyomtatása, joker (glob) minta használatával, és a megfelelő fájlokat nem tartalmazó könyvtárak kivágásával:

`tree -P '{{*.txt}}' --prune`

- Könyvtárak nyomtatása a fahierarchián belül, joker (glob) minta használatával, és azon könyvtárak kivágásával, amelyek nem a keresett könyvtár ősei:

`tree -P {{directory_name}} --matchdirs --prune`

- A fa kinyomtatása a megadott könyvtárak figyelmen kívül hagyásával:

`tree -I '{{directory_name1|directory_name2}}'`
