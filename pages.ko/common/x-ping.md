# x ping

> 향상된 ping 기능을 제공하는 모듈.
> 더 많은 정보: <https://x-cmd.com/mod/ping>.

- 지정한 호스트에 Ping 실행 (생략 시 기본값은 bing.com):

`x ping {{호스트}}`

- Ping 결과를 히트맵으로 표시:

`x ping {{[-m|--heatmap]}} {{호스트}}`

- Ping 결과를 막대 그래프로 표시:

`x ping {{[-b|--bar]}} {{호스트}}`

- Ping 결과를 처리해 히트맵으로 표시:

`ping {{호스트}} | x ping vis {{[-m|--heatmap]}}`

- 도움말 표시:

`x ping {{[-h|--help]}}`
