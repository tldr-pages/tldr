# babel

> 코드를 JavaScript ES6/ES7 문법에서 ES5 문법으로 변환하는 변환기입니다.
> 더 많은 정보: <https://babeljs.io/>.

- 지정된 입력 파일을 변환하고 `stdout'으로 출력:

`babel {{path/to/file}}`

- 지정된 입력 파일을 변환하고 특정 파일로 출력:

`babel {{path/to/input_file}} --out-file {{path/to/output_file}}`

- 입력 파일이 변경될 때마다 변환:

`babel {{path/to/input_file}} --watch`

- 파일의 전체 디렉토리를 변환:

`babel {{path/to/input_directory}}`

- 디렉토리에서 지정된 쉼표로 구분된 파일 무시:

`babel {{path/to/input_directory}} --ignore {{ignored_files}}`

- 축소된 JavaScript로 변환 및 출력:

`babel {{path/to/input_file}} --minified`

- 출력 형식에 대한 사전 설정 세트를 선택:

`babel {{path/to/input_file}} --presets {{presets}}`

- 사용 가능한 모든 옵션 출력:

`babel --help`
