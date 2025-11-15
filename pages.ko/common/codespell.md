# codespell

> 소스 코드에 대한 맞춤범 검사기.
> 더 많은 정보: <https://github.com/codespell-project/codespell>.

- 현재 디렉터리에 있는 모든 텍스트 파일의 오타를 재귀적으로 확인:

`codespell`

- 발견된 모든 오타를 수정:

`codespell --write-changes`

- 지정된 패턴과 일치하는 이름을 가진 파일을 건너뜀 (와일드카드를 사용하여 쉼표로 구분된 패턴 목록 허용):

`codespell --skip "{{패턴}}"`

- 확인할 때 사용자 정의사전 파일을 사용 (`--dictionary`는 여러 번 사용될 수 있음):

`codespell --dictionary {{경로/대상/파일.txt}}`

- 지정된 파일에 나열된 단어를 확인해서는 안 됨:

`codespell --ignore-words {{경로/대상/파일.txt}}`

- 지정된 단어를 확인하지 않음:

`codespell --ignore-words-list {{무시되는_단어1,무시되는_단어2,...}}`

- 각 매치되는 전후에, 3줄의 컨텍스트를 출력:

`codespell --{{context|before-context|after-context}} {{3}}`

- 파일 내용 외에도, 파일 이름에 오타가 있는지 확인:

`codespell --check-filenames`
