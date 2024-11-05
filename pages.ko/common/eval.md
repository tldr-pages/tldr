# eval

> 현재 쉘에서 인수를 단일 명령으로 실행하고 그 결과를 반환.
> 더 많은 정보: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#eval>.

- "foo" 인수를 사용하여 `echo`를 호출:

`eval "{{echo foo}}"`

- 현재 쉘에서 변수를 설정:

`eval "{{foo=bar}}"`
