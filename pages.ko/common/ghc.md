# ghc

> Glasgow Haskell 컴파일러.
> 하스켈 소스 파일을 컴파일하고 링크.
> 더 많은 정보: <https://downloads.haskell.org/ghc/latest/docs/users_guide/usage.html>.

- 현재 디렉터리에서 모든 모듈을 찾아 컴파일:

`ghc Main`

- 단일 파일 컴파일:

`ghc {{경로/대상/파일.hs}}`

- 추가 최적화를 사용해 컴파일:

`ghc -O {{경로/대상/파일.hs}}`

- 객체 파일(.o) 생성 후 컴파일 중지:

`ghc -c {{경로/대상/파일.hs}}`

- REPL (대화형 쉘)을 시작:

`ghci`

- 단일 표현식 평가:

`ghc -e {{표현식}}`
