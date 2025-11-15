# reportbug

> Debian 배포판의 버그 보고 도구.
> 더 많은 정보: <https://manned.org/reportbug>.

- 특정 패키지에 대한 버그 보고서를 작성하고 이메일로 전송:

`reportbug {{패키지}}`

- 특정 패키지와 관련 없는 버그(일반 문제, 인프라 등) 보고:

`reportbug other`

- 버그 보고서를 이메일로 보내지 않고 파일에 작성:

`reportbug -o {{파일명}} {{패키지}}`
