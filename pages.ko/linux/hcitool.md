# hcitool

> Bluetooth 장치에 연결을 모니터링, 구성하고 특수 명령을 전송합니다.
> 더 많은 정보: <https://manned.org/hcitool>.

- Bluetooth 장치 검색:

`hcitool scan`

- 장치의 이름을 출력하고 MAC 주소 반환:

`hcitool name {{bdaddr}}`

- 원격 Bluetooth 장치 정보 가져오기:

`hcitool info {{bdaddr}}`

- Bluetooth 장치와의 연결 품질 확인:

`hcitool lq {{bdaddr}}`

- 전송 전력 수준 수정:

`hcitool tpl {{bdaddr}} {{0|1}}`

- 연결 정책 표시:

`hcitool lp`

- 특정 장치와 인증 요청:

`hcitool auth {{bdaddr}}`

- 로컬 장치 표시:

`hcitool dev`
