# xgettext

> 코드 파일에서 gettext 문자열 추출.
> 더 많은 정보: <https://www.gnu.org/software/gettext/manual/gettext.html#xgettext-Invocation>.

- 파일을 스캔하고 문자열을 `messages.po`에 출력:

`xgettext {{경로/대상/입력_파일}}`

- 다른 출력 파일 이름 사용:

`xgettext {{[-o|--output]}} {{경로/대상/출력_파일}} {{경로/대상/입력_파일}}`

- 새 문자열을 기존 파일에 추가:

`xgettext {{[-j|--join-existing]}} {{[-o|--output]}} {{경로/대상/출력_파일}} {{경로/대상/입력_파일}}`

- 메타데이터를 포함하는 헤더를 출력 파일에 추가하지 않음:

`xgettext --omit-header {{경로/대상/입력_파일}}`
