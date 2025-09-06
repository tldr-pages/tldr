# fakeroot

> 파일 조작을 위해 루트 권한을 가장하는 환경에서 명령을 실행.
> 더 많은 정보: <https://manned.org/fakeroot.1>.

- fakeroot로 기본 셸 시작:

`fakeroot`

- fakeroot로 명령 실행:

`fakeroot -- {{명령어}} {{명령_인자들}}`

- fakeroot로 명령을 실행하고 종료 시 환경을 파일에 저장:

`fakeroot -s {{경로/대상/파일}} -- {{명령어}} {{명령_인자들}}`

- fakeroot 환경을 불러와 명령을 실행:

`fakeroot -i {{경로/대상/파일}} -- {{명령어}} {{명령_인자들}}`

- 파일의 실제 소유권을 유지하면서 명령 실행 (루트 소유로 가장하지 않음):

`fakeroot --unknown-is-real -- {{명령어}} {{명령_인자들}}`

- 도움말 표시:

`fakeroot --help`
