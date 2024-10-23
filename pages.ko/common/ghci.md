# ghci

> Glasgow Haskell 컴파일러 대화형 환경.
> 더 많은 정보: <https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>.

- REPL (대화형 쉘)을 시작:

`ghci`

- REPL을 시작하고 지정된 Haskell 소스 파일을 로드:

`ghci {{소스_파일.hs}}`

- REPL을 시작하고 언어 옵션을 활성화:

`ghci -X{{언어_옵션}}`

- REPL을 시작하고 일젓 수준의 컴파일러 경고(예: `all` 또는 `compact`)를 활성화:

`ghci -W{{경고_수준}}`

- 소스 파일을 찾기 위해 콜론으로 구분된 디렉터리 목록으로 REPL을 시작:

`ghci -i{{경로/대상/디렉터리1:경로/대상/디렉터리2:...}}`
