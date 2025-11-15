# sshpass

> SSH 비밀번호 제공 도구.
> TTY를 생성하고 비밀번호를 입력한 후 `stdin`을 SSH 세션으로 리디렉션하여 작동합니다.
> 더 많은 정보: <https://manned.org/sshpass>.

- 파일 디스크립터(이 경우, `stdin`)에 제공된 비밀번호를 사용하여 원격 서버에 연결:

`sshpass -d {{0}} ssh {{사용자}}@{{호스트명}}`

- 옵션으로 제공된 비밀번호를 사용하여 원격 서버에 연결하고, 알 수 없는 SSH 키를 자동으로 수락:

`sshpass -p {{비밀번호}} ssh -o StrictHostKeyChecking=no {{사용자}}@{{호스트명}}`

- 파일의 첫 번째 줄을 비밀번호로 사용하여 원격 서버에 연결하고, 알 수 없는 SSH 키를 자동으로 수락하며 명령 실행:

`sshpass -f {{경로/대상/파일}} ssh -o StrictHostKeyChecking=no {{사용자}}@{{호스트명}} "{{명령}}"`
