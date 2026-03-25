# clock

> 시스템 시계를 설정합니다.
> 더 많은 정보: <https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/command/reference/cf_book/cf_c1.html#clock>.

- 특권 모드에서 실행하여 시스템 시계를 설정:

`clock set {{23}}:{{59}}:{{59}} {{31}} {{april}} {{2000}}`

- 링크 반대편과 자동 협상, (기본값: active-clock):

`clock active prefer`

- 링크 반대편과 자동 협상, (기본값: passive-clock):

`clock passive prefer`

- 펌웨어에서 협상된 현재 clock 모드 확인:

`clock show interfaces`
