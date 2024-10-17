# fastmod

> codemod 도구에 대한 빠른 부분 교체, 전체 코드베이스에서 부분 및 모두 교체.
> 정규식은 Rust 정규식 상자와 일치.
> 더 많은 정보: <https://github.com/facebookincubator/fastmod>.

- .ignore 및 .gitignore의 파일을 무시하고 현재 디렉터리의 모든 파일에서 정규식 패턴을 변경:

`fastmod {{정규표현식_패턴}} {{대체문자열}}`

- 특정 파일이나 디렉터리에서 대소문자 구분 모드로 정규식 패턴을 변경:

`fastmod --ignore-case {{정규표현식_패턴}} {{대체문자열}} -- {{경로/대상/파일 경로/대상/디렉터리 ...}}`

- 대소문자를 구분하지 않는 glob 패턴으로 필터링된 파일의 특정 디렉터리에 있는 정규식 패턴을 변경:

`fastmod {{regex}} {{대체문자열}} --dir {{경로/대상/디렉터리}} --iglob {{'**/*.{js,json}'}}`

- `.js` 또는 JSON 파일에서 정확한 문자열 변경을 수행:

`fastmod --fixed-strings {{완전한_문자열}} {{대체문자열}} --extensions {{json,js}}`

- 확인 메시지 없이 정확한 문자열 바꾸기 (정규식 비활성화):

`fastmod --accept-all --fixed-strings {{완전한_문자열}} {{대체문자열}}`

- 확인 메시지 없이 정확한 문자열을 교체하고, 변경된 파일을 출력:

`fastmod --accept-all --print-changed-files --fixed-strings {{완전한_문자열}} {{대체문자열}}`
