# grep

> 정규표현식으로 파일에서 패턴을 찾습니다.
> 더 많은 정보: <https://www.gnu.org/software/grep/manual/grep.html>.

- 파일 안에서 패턴을 검색:

`grep "{{검색_패턴}}" {{파일/의/경로}}`

- 정규표현식을 사용하지 않고 정확히 일치하는 문자열 검색:

`grep --fixed-strings "{{문자열}}" {{파일/의/경로}}`

- 재귀적으로 디렉토리 안의 바이너리 파일을 제외한 모든 파일 안에서 패턴을 검색하고, 일치하는 줄의 번호를 보여줌:

`grep --recursive --line-number --binary-files={{without-match}} "{{검색_패턴}}" {{디렉토리/의/경로}}`

- 대소문자를 구분하지 않는 모드에서 확장된 정규표현식 사용 (`?`, `+`, `{}`, `()` 그리고 `|` 를 지원):

`grep --extended-regexp --ignore-case "{{검색_패턴}}" {{파일/의/경로}}`

- 일치하는 문자열 주변, 이전 혹은 이후의 3줄을 출력:

`grep --{{context|before-context|after-context}}={{3}} "{{검색_패턴}}" {{파일/의/경로}}`

- 각각의 일치하는 문자열의 파일 이름과 줄 번호 출력:

`grep --with-filename --line-number "{{검색_패턴}}" {{파일/의/경로}}`

- 패턴과 일치하는 줄을 검색하고, 일치하는 문자만 출력:

`grep --only-matching "{{검색_패턴}}" {{파일/의/경로}}`

- 패턴과 일치하지 않는 라인에 대한 stdin 검색:

`cat {{파일/의/경로}} | grep --invert-match "{{검색_패턴}}"`
