# hdparm

> SATA 및 IDE 하드 드라이브 매개변수를 조회하고 설정합니다.
> 더 많은 정보: <https://manned.org/hdparm>.

- 지정된 장치의 식별 정보 요청:

`sudo hdparm -I {{/dev/장치}}`

- 고급 전원 관리 수준 확인:

`sudo hdparm -B {{/dev/장치}}`

- 고급 전원 관리 값 설정 (1-127은 스핀 다운 허용, 128-254는 허용하지 않음):

`sudo hdparm -B {{1}} {{/dev/장치}}`

- 장치의 현재 전원 모드 상태 표시:

`sudo hdparm -C {{/dev/장치}}`

- 드라이브를 즉시 대기 모드로 전환 (대개 드라이브가 스핀 다운 됨):

`sudo hdparm -y {{/dev/장치}}`

- 드라이브를 대기(저전력) 모드로 전환하고 대기 시간 초과 설정:

`sudo hdparm -S {{대기_시간_초과}} {{장치}}`

- 특정 장치의 읽기 속도 테스트:

`sudo hdparm -tT {{장치}}`
