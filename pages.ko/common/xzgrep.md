# xzgrep

> 정규식을 사용하여 `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, 또는 `zstd`로 압축된 파일을 검색합니다.
> 같이 보기: `grep`.
> 더 많은 정보: <https://manned.org/xzgrep>.

- 파일 내 패턴 검색:

`xzgrep "{{검색_패턴}}" {{경로/대상/파일}}`

- 정확한 문자열 검색 (정규식 사용 안 함):

`xzgrep --fixed-strings "{{정확한_문자열}}" {{경로/대상/파일}}`

- 모든 파일에서 패턴을 검색하고 일치하는 줄 번호 표시:

`xzgrep --line-number "{{검색_패턴}}" {{경로/대상/파일}}`

- 확장 정규식(지원: `?`, `+`, `{}`, `()` 및 `|`)과 대소문자 구분 없는 모드 사용:

`xzgrep --extended-regexp --ignore-case "{{검색_패턴}}" {{경로/대상/파일}}`

- 각 일치 항목 주변, 이전 또는 이후에 3줄의 컨텍스트 출력:

`xzgrep --{{context|before-context|after-context}}={{3}} "{{검색_패턴}}" {{경로/대상/파일}}`

- 각 일치 항목에 대해 파일 이름과 줄 번호를 색상 출력으로 표시:

`xzgrep --with-filename --line-number --color=always "{{검색_패턴}}" {{경로/대상/파일}}`

- 패턴과 일치하는 줄을 검색하고 일치하는 텍스트만 출력:

`xzgrep --only-matching "{{검색_패턴}}" {{경로/대상/파일}}`
