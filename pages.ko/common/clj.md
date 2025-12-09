# clj

> REPL을 시작하거나 데이터로 함수를 호출하는 Clojure 도구.
> 모든 옵션은 `deps.edn` 파일에서 정의할 수 있음.
> 더 많은 정보: <https://clojure.org/guides/deps_and_cli>.

- REPL를 시작 (대화형 쉘):

`clj`

- 함수의 실행:

`clj -X {{네임스페이스/함수_이름}}`

- 지정된 네임스페이스의 기본 기능을 실행:

`clj -M -m {{네임스페이스}} {{args}}`

- 의존성을 해결하고, 라이브러리를 다운로드하고, 클래스 경로를 생성/캐싱하여 프로젝트를 준비:

`clj -P`

- CIDER 미들웨어로 nREPL 서버를 시작:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- ClojureScript용 REPL을 시작하고 웹 브라우저를 열기:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`
