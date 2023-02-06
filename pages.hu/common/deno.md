# deno

> Biztonságos futtatási idő JavaScripthez és TypeScripthez. További információ: <https://deno.land>.

- JavaScript vagy TypeScript fájl futtatása:

`deno run {{path/to/file.ts}}`

- Indítson el egy REPL-t (interaktív héj):

`deno`

- Futtasson egy fájlt hálózati hozzáférés engedélyezésével:

`deno run --allow-net {{path/to/file.ts}}`

- Fájl futtatása URL-címről:

`deno run {{https://deno.land/std/examples/welcome.ts}}`

- Futtatható szkript telepítése egy URL-címről:

`deno install {{https://deno.land/std/examples/colors.ts}}`
