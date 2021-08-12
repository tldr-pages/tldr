# ncc

> Compilați o aplicație Node.js într-un singur fișier.
> Suportă TypeScript, addons binare și necesită dinamic.
> Mai multe informaţii: <https://github.com/vercel/ncc>

- Pachet o aplicaţie Node.js:

`ncc build {{path/to/file.js}}`

- Bundle și minify o aplicație Node.js:

`ncc build --minify {{path/to/file.js}}`

- Bundle și minify o aplicație Node.js și generează hărți sursă:

`ncc build --source-map {{path/to/file.js}}`

- Recompilarea automată a modificărilor la fișierele sursă:

`ncc build --watch {{path/to/file.js}}`

- Bundați o aplicație Node.js într-un director temporar și rulați-l pentru testare:

`ncc run {{path/to/file.js}}`

- Curățați cache-ul `ncc`:

`ncc clean cache`
