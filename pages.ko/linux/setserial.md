# setserial

> 시리얼 포트 정보를 읽고 수정합니다.
> 더 많은 정보: <https://manned.org/setserial>.

- 특정 시리얼 장치에 대한 모든 정보 출력:

`setserial -a {{/dev/cuaN}}`

- 특정 시리얼 장치의 구성 요약 출력 (부팅 과정에서 출력할 때 유용):

`setserial -b {{장치}}`

- 장치에 특정 구성 매개변수 설정:

`sudo setserial {{장치}} {{매개변수}}`

- 장치 목록의 구성 출력:

`setserial -g {{장치1 장치2 ...}}`
