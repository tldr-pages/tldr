# git remote

> Nyomon követett adattárak ("remote"-ok) kezelése. További információ: <https://git-scm.com/docs/git-remote>.

- Megjeleníti a meglévő távoli tárolók listáját, azok nevét és URL-címét:

`git remote -v`

- Információk megjelenítése egy távoli elérhetőségről:

`git remote show {{remote_name}}`

- Távoli kapcsolat hozzáadása:

`git remote add {{remote_name}} {{remote_url}}`

- A távoli elérhetőség URL-jének módosítása (a `--add` használatával megtarthatja a meglévő URL-t):

`git remote set-url {{remote_name}} {{new_url}}`

- Egy távoli eszköz URL-címének megjelenítése:

`git remote get-url {{remote_name}}`

- Távirányító eltávolítása:

`git remote remove {{remote_name}}`

- Távoli kapcsolat átnevezése:

`git remote rename {{old_name}} {{new_name}}`
