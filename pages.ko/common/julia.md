# julia

> 기술 컴퓨팅을 위한 고수준, 고성능 동적 프로그래밍 언어.
> 더 많은 정보: <https://docs.julialang.org/en/v1/manual/getting-started/>.

- REPL(대화형 셸) 시작:

`julia`

- Julia 프로그램 실행 후 종료:

`julia {{프로그램.jl}}`

- 인자를 받는 Julia 프로그램 실행:

`julia {{프로그램.jl}} {{인자_목록}}`

- Julia 코드를 포함한 문자열 평가:

`julia -e '{{julia_코드}}'`

- 인자를 전달하며 Julia 코드 문자열 평가:

`julia -e '{{for x in ARGS; println(x); end}}' {{인자_목록}}`

- 표현식을 평가하고 결과 출력:

`julia -E '{{(1 - cos(pi/4))/2}}'`

- N개의 스레드를 사용하여 멀티스레드 모드로 Julia 시작:

`julia -t {{N}}`
