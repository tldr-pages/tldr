# inkmake

> Inkscape의 백엔드를 사용하여 GNU Makefile 스타일 SVG 내보내기.
> 더 많은 정보: <https://github.com/wader/inkmake>.

- 지정된 Inkfile을 실행하는 SVG 파일 내보내기:

`inkmake {{경로/대상/Inkfile}}`

- Inkfile을 실행하고 자세한 정보를 표시:

`inkmake --verbose {{경로/대상/Inkfile}}`

- SVG 입력 파일과 출력 파일을 지정하여, Inkfile을 실행:

`inkmake --svg {{경로/대상/파일.svg}} --out {{경로/대상/출력_이미지}} {{경로/대상/Inkfile}}`

- 사용자 정의 Inkscape 바이너리를 백엔드로 사용:

`inkmake --inkscape {{/Applications/Inkscape.app/Contents/Resources/bin/inkscape}} {{경로/대상/Inkfile}}`

- 도움말 표시:

`inkmake --help`
