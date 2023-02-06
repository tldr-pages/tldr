# esbuild

> JavaScript bundler és minifier a sebesség érdekében. További információ: <https://esbuild.github.io/>.

- JavaScript-alkalmazás csomagolása és nyomtatása a `stdout` címre:

`esbuild --bundle {{path/to/file.js}}`

- JSX-alkalmazás csomagolása a `stdin`:

`esbuild --bundle --outfile={{path/to/out.js}} < {{path/to/file.jsx}}`

- JSX-alkalmazás csomagolása és kicsinyítése a `production` módban a forrástérképekkel:

`esbuild --bundle --define:{{process.env.NODE_ENV=\"production\"}} --minify --sourcemap {{path/to/file.js}}`

- JSX-alkalmazás csomagolása böngészők vesszővel elválasztott listájához:

`esbuild --bundle --minify --sourcemap --target={{chrome58,firefox57,safari11,edge16}} {{path/to/file.jsx}}`

- JavaScript-alkalmazás csomagolása egy adott node-verzióhoz:

`esbuild --bundle --platform={{node}} --target={{node12}} {{path/to/file.js}}`

- JavaScript-alkalmazás csomagolása, amely lehetővé teszi a JSX-szintaxist a `.js` fájlokban:

`esbuild --bundle app.js --loader:{{.js=jsx}} {{path/to/file.js}}`

- JavaScript-alkalmazás csomagolása és kiszolgálása HTTP-kiszolgálón:

`esbuild --bundle --serve={{port}} --outfile={{index.js}} {{path/to/file.js}}`

- Fájlok listájának csomagolása egy kimeneti könyvtárba:

`esbuild --bundle --outdir={{path/to/output_directory}} {{path/to/file1 path/to/file2 ...}}`
