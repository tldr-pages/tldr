# msgcat

> 여러 개의 `.po` 번역 파일을 연결하거나 병합.
> 소프트웨어 현지화 과정에서 메시지 카탈로그를 결합하는 데 사용.
> 더 많은 정보: <https://www.gnu.org/software/gettext/manual/gettext.html#msgcat-Invocation>.

- 여러 `.po` 파일을 하나로 병합:

`msgcat {{파일1.po 파일2.po ...}} {{[-o|--output-file]}} {{병합된_파일.po}}`

- 텍스트 파일에 나열된 입력 파일들을 병합:

`msgcat {{[-f|--files-from]}} {{path/to/file_list.txt}} {{[-o|--output-file]}} {{병합된_파일.po}}`

- 출력 인코딩 지정 (예: UTF-8):

`msgcat {{[-t|--to-code]}} {{UTF-8}} {{입력_파일.po}} {{[-o|--output-file]}} {{출력_파일.po}}`

- 한 파일에만 존재하는 고유 메시지만 출력:

`msgcat {{[-u|--unique]}} {{파일1.po 파일2.po ...}} {{[-o|--output-file]}} {{고유_파일.po}}`

- 중복 메시지의 경우, 첫 번째 번역을 사용:

`msgcat --use-first {{파일1.po 파일2.po ...}} {{[-o|--output-file]}} {{출력_파일.po}}`

- 도움말 표시:

`msgcat {{[-h|--help]}}`
