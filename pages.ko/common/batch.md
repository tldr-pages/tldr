# batch

> 시스템 부하가 허용하는 시점에 명령을 실행.
> 실행 결과는 사용자의 이메일로 전송됨.
> 관련 항목: `at`, `atq`, `atrm`, `mail`.
> 더 많은 정보: <https://manned.org/batch>.

- `stdin`에서 명령을 입력받아 실행 예약(입력 완료 시 `<Ctrl d>` 누르기):

`batch`

- `stdin`에서 명령을 전달받아 실행 예약:

`echo "{{./make_db_backup.sh}}" | batch`
