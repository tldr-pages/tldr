# audit2allow

> SELinux 로컬 정책 모듈을 생성하여 로그에 기록된 거부된 작업 기반의 규칙을 허용합니다.
> 관련 항목: `audit2why`, `ausearch`, `semodule`.
> 더 많은 정보: <https://manned.org/audit2allow>.

- 거부된 모든 서비스에 대한 접근을 허용하는 로컬 정책 생성:

`sudo audit2allow --all -M {{로컬_정책_이름}}`

- 감사 로그에서 특정 프로세스/서비스/명령에 대한 접근을 허용하는 로컬 정책 모듈 생성:

`sudo grep {{apache2}} /var/log/audit/audit.log | sudo audit2allow -M {{로컬_정책_이름}}`

- 로컬 정책의 Type Enforcement (.te) 파일을 검사하고 검토:

`vim {{로컬_정책_이름}}.te`

- 로컬 정책 모듈 설치:

`sudo semodule -i {{로컬_정책_이름}}.pp`
