# turbo

> Nagy teljesítményű build rendszer JavaScript és TypeScript kódbázisokhoz. Lásd még: `nx`. További információ: <https://turborepo.org/docs/reference/command-line-reference>.

- Jelentkezzen be az alapértelmezett webböngészővel egy Vercel-fiókkal:

`turbo login`

- Kapcsolja az aktuális könyvtárat egy Vercel-szervezethez, és engedélyezze a távoli gyorsítótárazást:

`turbo link`

- Építse az aktuális projektet:

`turbo run build`

- Futtasson egy feladatot párhuzamosság nélkül:

`turbo run {{task_name}} --concurrency={{1}}`

- Futtasson egy feladatot a gyorsítótárazott leletek figyelmen kívül hagyásával, és kényszerítse ki az összes feladat újbóli végrehajtását:

`turbo run {{task_name}} --force`

- Feladat futtatása párhuzamosan a csomagok között:

`turbo run {{task_name}} --parallel --no-cache`

- Az aktuális könyvtár függetlenítése a Vercel-szervezettől és a távoli gyorsítótárazási funkció letiltása:

`turbo unlink`

- Dot-grafikon generálása egy adott feladat végrehajtásáról (a kimeneti fájlformátum a fájlnévvel szabályozható):

`turbo run {{task_name}} --graph={{path/to/file}}.{{html|jpg|json|pdf|png|svg}}`
