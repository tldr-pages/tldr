# rlwrap

> REPL 명령에 라인 편집, 지속적인 히스토리 및 프롬프트 완성을 추가.
> 더 많은 정보: <https://manned.org/rlwrap>.

- 라인 편집, 지속적인 히스토리 및 프롬프트 완성을 사용하여 REPL 명령 실행:

`rlwrap {{명령}}`

- 입력 및 출력에서 본 모든 단어를 프롬프트 완성에 사용:

`rlwrap --remember {{명령}}`

- 프롬프트에 ANSI 색상 코드가 포함된 경우 더 나은 프롬프트 완성:

`rlwrap --ansi-colour-aware {{명령}}`

- 파일 이름 완성 활성화 (대소문자 구분):

`rlwrap --complete-filenames {{명령}}`

- 색상이 있는 프롬프트 추가, 색상 이름 또는 ASCI 색상 사양 사용. 대문자 색상 이름은 굵게 스타일링:

`rlwrap --prompt-colour={{black|red|green|yellow|blue|cyan|purple|white|colour_spec}} {{명령}}`
