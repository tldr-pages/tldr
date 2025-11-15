# pyinfra

> 대규모 인프라를 자동화.
> 더 많은 정보: <https://docs.pyinfra.com/en/3.x/cli.html>.

- SSH를 통해 명령 실행:

`pyinfra {{대상_IP_주소}} exec -- {{명령어_및_인수}}`

- 대상 목록에 있는 서버에 배포 파일의 내용을 실행:

`pyinfra {{경로/대상/목록.py}} {{경로/배포.py}}`

- 로컬에서 명령 실행:

`pyinfra @local {{경로/배포.py}}`

- Docker를 통해 명령 실행:

`pyinfra @docker/{{컨테이너}} {{경로/배포.py}}`
