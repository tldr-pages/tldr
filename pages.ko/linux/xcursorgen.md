# xcursorgen

> PNG 모음에서 X 커서 파일 생성.
> `--prefix`가 생략되면 이미지 파일은 현재 작업 디렉터리에 위치해야 합니다.
> 더 많은 정보: <https://manned.org/xcursorgen>.

- 구성 파일을 사용하여 X 커서 파일 생성:

`xcursorgen {{경로/대상/구성.cursor}} {{경로/대상/출력_파일}}`

- 구성 파일을 사용하여 X 커서 파일을 만들고 이미지 파일의 경로 지정:

`xcursorgen --prefix {{경로/대상/이미지_디렉터리/}} {{경로/대상/구성.cursor}} {{경로/대상/출력_파일}}`

- 구성 파일을 사용하여 X 커서 파일을 만들고 출력을 `stdout`에 쓰기:

`xcursorgen {{경로/대상/구성.cursor}}`
