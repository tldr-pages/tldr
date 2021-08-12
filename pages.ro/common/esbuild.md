# esbuild

> Pachet JavaScript și minifier construit pentru viteză.
> Mai multe informaţii: <https://esbuild.github.io/>

- Bundle o aplicație JavaScript și imprimați la stdout:

`esbuild --bundle {{path/to/file.js}}`

- Bundle o aplicatie JSX de la stdin:

`esbuild --bundle --outfile={{path/to/out.js}} < {{path/to/file.jsx}}`

- Bundați și minify o aplicație JSX cu hărți sursă în modul `producție':

`esbuild --bundle --define:{{process.env.NODE_ENV=\"production\"}} --minify --sourcemap {{path/to/file.js}}`

- Pachet o aplicație JSX pentru o listă separată prin virgulă de browsere:

`esbuild --bundle --minify --sourcemap --target={{chrome58,firefox57,safari11,edge16}} {{path/to/file.jsx}}`

- Bundle o aplicație JavaScript pentru o versiune de nod specific:

`esbuild --bundle --platform={{node}} --target={{node12}} {{path/to/file.js}}`

- Banda o aplicatie JavaScript ce permite sintaxa JSX in fisierele `.js`:

`esbuild --bundle app.js --loader:{{.js=jsx}} {{path/to/file.js}}`

- Bundați și serviți o aplicație JavaScript pe un server HTTP:

`esbuild --bundle --serve={{port}} --outfile={{index.js}} {{path/to/file.js}}`

- Bundați o listă de fișiere într-un director de ieșire:

`esbuild --bundle --outdir={{path/to/output_directory}} {{path/to/file1}} {{path/to/file2}}`
