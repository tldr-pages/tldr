# prettier

> JavaScript, JSON, CSS, YAML 등을 위한 명시적인 코드 포맷 도구.
> 더 많은 정보: <https://prettier.io/>.

- 파일 형식을 지정하고 결과를 `stdout`으로 출력:

`prettier {{경로/대상/파일}}`

- 특정 파일의 형식이 지정되었는지 확인:

`prettier --check {{경로/대상/파일}}`

- 특정 구성 파일로 실행:

`prettier --config {{경로/대상/설정_파일}} {{경로/대상/파일}}`

- 파일이나 폴더를 포맷하여 원본을 대체:

`prettier --write {{경로/대상/파일_또는_폴더}}`

- 작은따옴표를 사용하고 후행 쉼표를 사용하지 않고 파일 또는 폴더 형식을 반복적으로 지정:

`prettier --single-quote --trailing-comma {{none}} --write {{경로/대상/파일_또는_폴더}}`

- JavaScript 및 TypeScript 파일의 형식을 재귀적으로 지정하여 원본 대체:

`prettier --write "**/*.{js,jsx,ts,tsx}"`
