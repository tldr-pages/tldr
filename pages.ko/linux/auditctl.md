# auditctl

> Linux 감사 시스템의 동작을 제어하고 상태를 확인하며 규칙을 관리하는 유틸리티.
> 더 많은 정보: <https://manned.org/auditctl>.

- 감사 시스템의 [s]상태 표시:

`sudo auditctl -s`

- 현재 로드된 모든 감사 규칙 [l]목록:

`sudo auditctl -l`

- 모든 감사 규칙 [D]삭제:

`sudo auditctl -D`

- 감사 시스템 [e]활성화/비활성화:

`sudo auditctl -e {{1|0}}`

- 파일 변경 감시:

`sudo auditctl -a always,exit -F arch=b64 -F path={{/경로/대상/파일}} -F perm=wa`

- 디렉토리를 재귀적으로 변경 감시:

`sudo auditctl -a always,exit -F arch=b64 -F dir={{/경로/대상/폴더/}} -F perm=wa`

- [h]도움말 표시:

`auditctl -h`
