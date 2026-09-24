# aa-logprof

> 기록된 위반 로그를 기반으로 AppArmor 보안 프로파일을 대화형으로 업데이트하는 도구.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-logprof.8>.

- 시스템 로그를 기반으로 대화형으로 프로파일 검토 및 업데이트:

`sudo aa-logprof`

- AppArmor 프로파일 디렉터리 지정:

`sudo aa-logprof {{[-d|--dir]}} /{{경로/대상/프로파일}}`

- 기본 로그 대신 특정 로그 파일 사용:

`sudo aa-logprof {{[-f|--file]}} /{{경로/대상/로그파일}}`

- 지정한 마커 이전 로그 항목 무시:

`sudo aa-logprof {{[-m|--logmark]}} "{{로그_마커_텍스트}}"`

- 도움말 표시:

`aa-logprof {{[-h|--help]}}`
