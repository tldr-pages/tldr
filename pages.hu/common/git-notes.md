# git notes

> Objektumjegyzetek hozzáadása vagy megtekintése. További információ: <https://git-scm.com/docs/git-notes>.

- Az összes jegyzet és a hozzájuk tartozó objektumok listája:

`git notes list`

- Az adott objektumhoz csatolt összes jegyzet listázása (alapértelmezett beállítás: HEAD):

`git notes list [{{object}}]`

- Az adott objektumhoz csatolt jegyzetek megjelenítése (alapértelmezett beállítás: HEAD):

`git notes show [{{object}}]`

- Jegyzet csatolása egy megadott objektumhoz (megnyitja az alapértelmezett szövegszerkesztőt):

`git notes append {{object}}`

- Jegyzet csatolása egy megadott objektumhoz, az üzenet megadásával:

`git notes append --message="{{message_text}}"`

- Meglévő jegyzet szerkesztése (alapértelmezett beállítás: HEAD):

`git notes edit [{{object}}]`

- Jegyzet másolása egyik objektumból egy másikba:

`git notes copy {{source_object}} {{target_object}}`

- A megadott objektumhoz hozzáadott összes jegyzet eltávolítása:

`git notes remove {{object}}`
