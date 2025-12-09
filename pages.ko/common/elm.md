# elm

> Elm 소스 파일을 컴파일하고 실행.
> 더 많은 정보: <https://guide.elm-lang.org/install/elm.html>.

- Elm 프로젝트를 초기화하고, elm.json 파일을 생성:

`elm init`

- 대화형 Elm 쉘을 시작:

`elm repl`

- Elm 파일을 컴파일하고, 결과를 `index.html` 파일로 출력:

`elm make {{소스}}`

- Elm 파일을 컴파일하고, 결과를 JavaScript 파일로 출력:

`elm make {{소스}} --output={{대상}}.js`

- 페이지 로드 시 Elm 파일을 컴파일하는 로컬 웹 서버 시작:

`elm reactor`

- <https://package.elm-lang.org>에서 Elm 패키지를 설치:

`elm install {{저자}}/{{패키지}}`
