# rename

> 정규 표현식 (`regex`)을 사용하여 하나 이상의 파일 이름을 변경.
> 경고: dry-run 옵션을 사용하지 않으면 확인 없이 기존 파일을 덮어쓸 수 있음.
> 참고: 이 문서는 `file-rename`으로도 알려진 Perl 버전의, rename을 다룸.
> 더 많은 정보: <https://manned.org/prename>.

- 지정한 파일 이름에서 `from`을 `to`로 변경:

`rename 's/{{from}}/{{to}}/' {{*.txt}}`

- Dry-run 수행 - 실제 변경 없이 변경될 내용만 표시:

`rename -n 's/{{from}}/{{to}}/' {{*.txt}}`

- 파일 확장자 변경:

`rename 's/\.{{old}}$/\.{{new}}/' {{*.txt}}`

- 파일 이름을 소문자로 변경 (대소문자를 구분하지 않는 파일 시스템에서는 `-f` 사용):

`rename {{[-f|--force]}} 'y/A-Z/a-z/' {{*.txt}}`

- 파일 이름에서 각 단어의 첫 글자를 대문자로 변경:

`rename {{[-f|--force]}} 's/\b(\w)/\U$1/g' {{*.txt}}`

- 파일 이름의 공백을 밑줄로 변경:

`rename 's/\s+/_/g' {{*.txt}}`
