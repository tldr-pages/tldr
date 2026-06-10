# esbuild

> JavaScript փաթեթավորող և մինիֆիկատոր՝ ստեղծված արագության համար:.
> Լրացուցիչ տեղեկություններ. <https://esbuild.github.io/api/#general-options>:.

- Կազմեք JavaScript հավելված և տպեք `stdout`:

`esbuild --bundle {{path/to/file.js}}`

- Փաթեթավորեք JSX հավելված `stdin`-ից՝:

`esbuild < {{path/to/file.jsx}} --bundle --outfile={{path/to/out.js}}`

- Փաթեթավորեք և փոքրացրեք JSX հավելվածը աղբյուրի քարտեզներով `production` ռեժիմով.:

`esbuild --bundle --define:{{process.env.NODE_ENV=\"production\"}} --minify --sourcemap {{path/to/file.js}}`

- Փաթեթավորեք JSX հավելված բրաուզերների ստորակետերով բաժանված ցուցակի համար.:

`esbuild --bundle --minify --sourcemap --target={{chrome58,firefox57,safari11,edge16}} {{path/to/file.jsx}}`

- Միավորել JavaScript հավելվածը կոնկրետ հանգույցի տարբերակի համար.:

`esbuild --bundle --platform={{node}} --target={{node12}} {{path/to/file.js}}`

- Միավորել JavaScript հավելվածը, որը հնարավորություն է տալիս JSX շարահյուսությունը `.js` ֆայլերում.:

`esbuild --bundle app.js --loader:{{.js=jsx}} {{path/to/file.js}}`

- Փաթեթավորեք և մատուցեք JavaScript հավելվածը HTTP սերվերի վրա.:

`esbuild --bundle --serve={{port}} --outfile={{index.js}} {{path/to/file.js}}`

- Փաթեթավորեք ֆայլերի ցանկը ելքային գրացուցակում.:

`esbuild --bundle --outdir={{path/to/output_directory}} {{path/to/file1 path/to/file2 ...}}`
