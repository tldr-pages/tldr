# evtest

> 입력 장치 드라이버에서 정보를 표시합니다.
> 더 많은 정보: <https://manned.org/evtest>.

- 감지된 모든 입력 장치를 나열:

`sudo evtest`

- 특정 입력 장치에서 이벤트 표시:

`sudo evtest /dev/input/event{{번호}}`

- 장치를 독점적으로 점유하여 다른 클라이언트가 이벤트를 수신하지 못하도록 방지:

`sudo evtest --grab /dev/input/event{{번호}}`

- 입력 장치에서 특정 키 또는 버튼의 상태를 조회:

`sudo evtest --query /dev/input/event{{번호}} {{이벤트_타입}} {{이벤트_코드}}`
