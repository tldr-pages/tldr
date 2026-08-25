# aa-genprof

> 프로그램 동작을 모니터링하여 AppArmor 보안 프로파일을 생성하는 도구.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-genprof.8>.

- 프로그램에 대한 프로파일 생성 시작:

`sudo aa-genprof {{프로그램_경로}}`

- 프로파일 디렉터리 사용자 지정:

`sudo aa-genprof {{[-d|--dir]}} /{{경로/대상/프로파일}} {{프로그램_경로}}`

- 프로파일링에 사용할 로그 지정:

`sudo aa-genprof {{[-f|--file]}} /{{경로/대상/로그파일}} {{프로그램_경로}}`

- 도움말 표시:

`aa-genprof {{[-h|--help]}}`
