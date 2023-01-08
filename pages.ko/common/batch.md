# batch

> 시스템 로드 레벨이 허가된 후, 명령을 실행하십시오. 실제로 실행하기 위해서는 atd (혹은 atrun) 를 실행해야합니다.
> 더 많은 정보: <https://manned.org/batch>.

- 표준 입력에서 명령 실행하기 (완료 시 `Ctrl + D` 를 누릅니다):

`batch`

- 표준 입력에서의 명령 실행하기:

`echo "{{./make_db_backup.sh}}" | batch`

- 특정 파일에서 명령 실행하기:

`batch -f {{path/to/file}}`
