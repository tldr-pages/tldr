# systemctl set-property

> 특정 유닛 속성을 런타임에 설정.
> 관련 항목: `systemctl revert`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#set-property%20UNIT%20PROPERTY=VALUE%E2%80%A6>.

- 실행 중인 서비스의 속성 설정:

`systemctl set-property {{유닛}} {{속성}}={{값}}`

- 여러 속성을 한 번에 설정:

`systemctl set-property {{유닛}} {{속성_1=값_1 속성_2=값_2 ...}}`

- 현재 런타임 세션에만 적용 (영구 저장 아님):

`systemctl set-property {{유닛}} {{속성}}={{값}} --runtime`

- 속성을 기본값으로 초기화:

`systemctl set-property {{유닛}} {{속성}}=`

- 여러 속성을 기본값으로 초기화:

`systemctl set-property {{유닛}} {{속성_1= 속성_2= ...}}`
