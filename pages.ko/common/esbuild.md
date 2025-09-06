# esbuild

> 속도를 위해 제작된 자바스크립트 번들러 및 압축 도구.
> 더 많은 정보: <https://esbuild.github.io/>.

- 자바스크립트 애플리케이션을 번들로 묶어 `stdout`으로 인쇄:

`esbuild --bundle {{경로/대상/파일.js}}`

- `stdin`에서 JSX 애플리케이션 번들링:

`esbuild --bundle --outfile={{경로/대상/파일.js}} < {{경로/대상/파일.jsx}}`

- `production` 모드에서 소스맵을 사용하여 JSX 애플리케이션을 번들로 묶고 압축:

`esbuild --bundle --define:{{process.env.NODE_ENV=\"production\"}} --minify --sourcemap {{경로/대상/파일.js}}`

- 쉼표로 구분된 브라우저 목록을 위해 JSX 애플리케이션을 번들로 묶음:

`esbuild --bundle --minify --sourcemap --target={{chrome58,firefox57,safari11,edge16}} {{경로/대상/파일.jsx}}`

- 특정 노드 버전에 대한 자바스크립트 애플리케이션 번들:

`esbuild --bundle --platform={{node}} --target={{node12}} {{경로/대상/파일.js}}`

- `.js` 파일에 JSX 구문을 활성화하는 자바스크립트 애플리케이션을 번들로 묶음:

`esbuild --bundle app.js --loader:{{.js=jsx}} {{경로/대상/파일.js}}`

- HTTP 서버에서 자바스크립트 애플리케이션을 번들링하고 제공:

`esbuild --bundle --serve={{port}} --outfile={{index.js}} {{경로/대상/파일.js}}`

- 파일 목록을 출력 폴더에 번들링:

`esbuild --bundle --outdir={{경로/대상/출력_폴더}} {{경로/대상/파일1 경로/대상/파일2 ...}}`
