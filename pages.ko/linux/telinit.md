# telinit

> SysV 런레벨 변경.
> SysV 런레벨 개념은 더 이상 사용되지 않으므로 런레벨 요청은 시스템 단위 활성화 요청으로 투명하게 변환됩니다.
> 더 많은 정보: <https://manned.org/telinit>.

- 시스템 전원 끄기:

`telinit 0`

- 시스템 재부팅:

`telinit 6`

- SysV 런레벨 변경:

`telinit {{2|3|4|5}}`

- 복구 모드로 변경:

`telinit 1`

- 데몬 구성 다시 로드:

`telinit q`

- 재부팅/전원 끄기 전 사전 알림 메시지 전송 안 함 (6/0):

`telinit --no-wall {{값}}`
