# Xephyr

> X 애플리케이션으로 실행되는 중첩 X 서버.
> 더 많은 정보: <https://manned.org/xserver-xephyr>.

- 디스플레이 ID ":2"로 검은색 창 생성:

`Xephyr -br -ac -noreset -screen {{800x600}} {{:2}}`

- 새 화면에서 X 애플리케이션 시작:

`DISPLAY=:2 {{명령_이름}}`
