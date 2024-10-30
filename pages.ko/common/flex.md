# flex

> 어휘 분석기 생성기. POSIX 사양을 확장하여 `lex`.
> 어휘 분석기에 대한 사양이 주어지면 이를 구현하는 C 코드를 생성.
> 참고: OpenBSD에서는 긴 옵션이 작동하지 않음.
> 더 많은 정보: <https://manned.org/flex>.

- flex 파일에서 분석기를 생성하여, `lex.yy.c` 파일에 저장:

`lex {{analyzer.l}}`

- `stdout`에 분석기 쓰기:

`lex -{{-stdout|t}} {{analyzer.l}}`

- 출력 파일을 지정:

`lex {{analyzer.l}} -o {{analyzer.c}}`

- 대화형 스캐너 대신 [B]atch 스캐너를 생성:

`lex -B {{analyzer.l}}`

- Lex에서 생성된 C 파일을 컴파일:

`cc {{경로/대상/lex.yy.c}} --output {{executable}}`
