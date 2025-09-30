# rfkill

> 무선 장치를 활성화하거나 비활성화합니다.
> 더 많은 정보: <https://manned.org/rfkill>.

- 장치 나열:

`rfkill`

- 열로 필터링:

`rfkill -o {{ID,TYPE,DEVICE}}`

- 유형별로 장치 차단 (예: bluetooth, wlan):

`rfkill block {{bluetooth}}`

- 유형별로 장치 차단 해제 (예: bluetooth, wlan):

`rfkill unblock {{wlan}}`

- JSON 형식으로 출력:

`rfkill -J`
