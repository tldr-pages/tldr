# netselect

> 빠른 네트워크 서버 선택을 위한 속도 테스트.
> 더 많은 정보: <https://github.com/apenwarr/netselect>.

- 지연 시간이 가장 낮은 서버 선택:

`sudo netselect {{호스트_1}} {{호스트_2}}`

- 네임서버 해상도 및 통계 표시:

`sudo netselect -vv {{호스트_1}} {{호스트_2}}`

- 최대 TTL(수명) 정의:

`sudo netselect -m {{10}} {{호스트_1}} {{호스트_2}}`

- 호스트 중에서 가장 빠른 N개의 서버 출력:

`sudo netselect -s {{N}} {{호스트_1}} {{호스트_2}} {{호스트_3}}`

- 도움말 표시:

`netselect`
