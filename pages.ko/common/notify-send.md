# notify-send

> 현재 데스크톱 환경의 알림 시스템을 사용하여 알림을 생성합니다.
> 더 많은 정보: <https://manned.org/notify-send>.

- 제목 "Test"와 내용 "This is a test"로 알림 표시:

`notify-send "{{Test}}" "{{This is a test}}"`

- 사용자 지정 아이콘과 함께 알림 표시:

`notify-send -i {{아이콘.png}} "{{테스트}}" "{{이것은 테스트입니다}}"`

- 5초 동안 알림 표시:

`notify-send -t 5000 "{{테스트}}" "{{이것은 테스트입니다}}"`

- 앱의 아이콘과 이름으로 알림 표시:

`notify-send "{{Test}}" --icon={{google-chrome}} --app-name="{{Google Chrome}}"`
