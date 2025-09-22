# deno

> Un entorno de ejecución seguro para JavaScript, TypeScript y WebAssembly.
> Incluye gestión de dependencias usando `npm` o `jsr` y herramientas como bench, bundle, doc y coverage.
> Más información: <https://docs.deno.com/runtime/reference/cli>.

- Inicia un REPL (shell interactivo, también conocido como Read-Eval-Print Loop):

`deno`

- Inicia un nuevo proyecto llamado sample y lo prueba:

`deno init sample && cd sample && deno test`

- Ejecuta un archivo de forma segura. Preguntará (si es necesario) para permitir net, read, etc:

`deno run {{ruta/al/archivo.ts}}`

- Ejecuta un archivo con permisos explícitos o permite todo (solo si confías en la fuente):

`deno run {{[--allow-env|--allow-net|--allow-write|--allow-all]}} {{jsr:@deno/deployctl}}`

- Lista y ejecuta tareas desde `deno.json` o scripts desde `package.json`:

`deno task`

- Instala dependencias listadas en `deno.json` o `package.json` (también bloquea archivos):

`deno install`

- Comprueba tipos, formato y lint (corrige si es posible):

`deno check && deno fmt && deno lint --fix`

- Compila el script, las dependencias importadas y el entorno de ejecución en un ejecutable independiente:

`deno compile {{ruta/al/archivo.ts}}`
