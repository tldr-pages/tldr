# printf

> 텍스트를 형식화하여 출력.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html>.

- 텍스트 메시지 출력:

`printf "{{%s\n}}" "{{Hello world}}"`

- 정수를 굵은 파란색으로 출력:

`printf "{{\e[1;34m%.3d\e[0m\n}}" {{42}}`

- 유로 기호와 함께 실수 출력:

`printf "{{\u20AC %.2f\n}}" {{123.4}}`

- 환경 변수를 사용하여 구성된 텍스트 메시지 출력:

`printf "{{var1: %s\tvar2: %s\n}}" "{{$VAR1}}" "{{$VAR2}}"`

- 형식화된 메시지를 변수에 저장 (Zsh에서는 작동하지 않음):

`printf -v {{myvar}} {{"This is %s = %d\n" "a year" 2016}}`

- 16진수, 8진수 및 과학적 표기법 숫자 출력:

`printf "{{hex=%x octal=%o scientific=%e}}" 0x{{FF}} 0{{377}} {{100000}}`
