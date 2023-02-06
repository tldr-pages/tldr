# vercel

> A Vercel telepítések telepítése és kezelése. További információ: <https://vercel.com/docs/cli>.

- Az aktuális könyvtár telepítése:

`vercel`

- Az aktuális könyvtár telepítése a termelésbe:

`vercel --prod`

- Egy könyvtár telepítése:

`vercel {{path/to/project}}`

- Egy példaprojekt inicializálása:

`vercel init`

- Telepítés környezeti változókkal:

`vercel --env {{ENV}}={{var}}`

- Build with Environment Variables:

`vercel --build-env {{ENV}}={{var}}`

- Alapértelmezett régiók beállítása a telepítés engedélyezéséhez:

`vercel --regions {{region_id}}`

- Telepítés eltávolítása:

`vercel remove {{project_name}}`
