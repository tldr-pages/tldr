# gitsome

> Terminál alapú felület a GitHub-hoz, amely a `gh` paranccsal érhető el. A `git` parancsokhoz menüszerű automatikus kitöltési javaslatokat is biztosít. További információ: <https://github.com/donnemartin/gitsome>.

- Lépjen be a gitsome héjba (opcionális), hogy engedélyezze az automatikus kitöltést és az interaktív súgót a Git (és a gh) parancsokhoz:

`gitsome`

- GitHub integráció beállítása az aktuális fiókkal:

`gh configure`

- Az aktuális fiók értesítéseinek listázása (ahogyan az a https://github.com/notifications oldalon látható lenne):

`gh notifications`

- Az aktuális fiók csillagozott repos-ainak listázása, adott keresőszöveg alapján szűrve:

`gh starred "{{python 3}}"`

- Egy adott GitHub-tárhely legutóbbi aktivitásának megtekintése:

`gh feed {{tldr-pages/tldr}}`

- Egy adott GitHub-felhasználó legutóbbi tevékenységének megtekintése az alapértelmezett lapozó használatával (pl. `less`):

`gh feed {{torvalds}} -p`
