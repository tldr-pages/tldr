# dzdo

> Active Directory 역할을 통해 root 또는 다른 사용자 권한으로 명령을 실행하는 도구.
> `sudo`와 유사하지만 Delinea와 통합되어 있으며; Ansible의 become 플러그인을 지원.
> 더 많은 정보: <https://docs.delinea.com/online-help/server-suite/commandref/centrify-command-reference-2025.pdf#page=102>.

- 권한 상승하여 명령 실행:

`dzdo {{명령어}}`

- 다른 사용자로 명령 실행:

`dzdo -u {{사용자}} {{명령어}}`

- 기본 편집기로 파일을 권한 상승하여 편집:

`dzdo -e {{경로/대상/파일}}`

- 권한 상승된 대화형 로그인 쉘 실행:

`dzdo -i`

- 기본 쉘을 권한 상승하여 실행:

`dzdo -s`

- 현재 사용자가 실행 가능한 명령 목록 출력:

`dzdo -l`

- 인증 상태 확인 및 타임스탬프 갱신:

`dzdo -v`

- 버전 정보 표시:

`dzdo -V`
