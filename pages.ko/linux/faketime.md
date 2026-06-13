# faketime

> 명령어에 대해 시스템 시간을 속입니다.
> 더 많은 정보: <https://manned.org/faketime>.

- `date` 명령의 결과를 출력하기 전에 시간을 오늘 저녁으로 설정:

`faketime '{{today 23:30}}' {{date}}`

- 어제를 현재 날짜로 사용하는 새로운 Bash 셸 열기:

`faketime '{{yesterday}}' {{bash}}`

- 다음 주 금요일 밤에 프로그램이 어떻게 작동할지 시뮬레이션:

`faketime '{{next Friday 1 am}}' {{경로/대상/프로그램}}`
