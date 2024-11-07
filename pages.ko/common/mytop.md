# mytop

> MySQL 서버 성능 정보를 `top`처럼 표시.
> 더 많은 정보: <https://jeremy.zawodny.com/mysql/mytop/mytop.html>.

- `mytop` 시작:

`mytop`

- 지정된 사용자 이름과 비밀번호로 연결:

`mytop -u {{사용자}} -p {{비밀번호}}`

- 지정된 사용자 이름으로 연결 (비밀번호 입력이 요청됨):

`mytop -u {{사용자}} --prompt`

- 유휴(대기) 스레드를 표시하지 않음:

`mytop -u {{사용자}} -p {{비밀번호}} --noidle`
