# noglob

> Zsh에서 globbing(wildcard 패턴 확장) 없이 명령을 실행.
> 더 많은 정보: <https://manned.org/zshmisc>.

- 따옴표나 이스케이프 없이 URL 요청:

`noglob curl {{https://example.com?a=1}}`

- 이름에 리터럴 별표가 포함된 파일 열기:

`noglob less {{*.txt}}`
