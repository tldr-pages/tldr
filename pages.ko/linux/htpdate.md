# htpdate

> 웹 서버의 HTTP 헤더를 통해 로컬 날짜 및 시간을 동기화합니다.
> 더 많은 정보: <https://www.vervest.org/htp/>.

- 날짜와 시간 동기화:

`sudo htpdate {{호스트}}`

- 동기화 시뮬레이션 수행, 실제 동작은 없음:

`htpdate -q {{호스트}}`

- 체계적인 시계 드리프트 보정:

`sudo htpdate -x {{호스트}}`

- 동기화 후 즉시 시간 설정:

`sudo htpdate -s {{호스트}}`
