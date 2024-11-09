# unimatrix

> 유니코드 문자를 사용하여 매트릭스 느낌을 시뮬레이션.
> 같이 보기: `cmatrix`.
> 더 많은 정보: <https://github.com/will8211/unimatrix>.

- `cmatrix`의 기본 출력을 모방 (유니코드 없이, TTY에서 작동):

`unimatrix --no-bold --speed {{96}} --character-list {{o}}`

- 볼드체 없이, 느리게, 이모지, 숫자 및 일부 기호 사용:

`unimatrix --no-bold --speed {{50}} --character-list {{ens}}`

- 문자 색상 변경:

`unimatrix --color {{red|green|blue|white|...}}`

- 문자 집합을 코드로 선택 (`unimatrix --help`에서 사용 가능한 문자 집합 확인):

`unimatrix --character-list {{문자_집합}}`

- 스크롤 속도 변경:

`unimatrix --speed {{숫자}}`
