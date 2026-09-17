# batch

> 시스템 부하가 허용하는 시점에 명령을 나중에 실행.
> 실행 결과는 사용자 메일로 전송됨.
> 관련 항목: `at`, `atq`, `atrm`, `mail`.
> 더 많은 정보: <https://manned.org/batch>.

- `atd` 데몬 시작:

`systemctl start atd`

- `stdin`으로부터 명령 실행 (`<Ctrl d>` 입력 시 종료):

`batch`

- `stdin`으로부터 단일 명령 실행:

`echo "{{./db_백업_생성_스크립트.sh}}" | batch`
