# aa-audit

> AppArmor 보안 프로파일을 audit 모드로 설정.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-audit.8>.

- 프로파일을 audit 모드로 설정:

`sudo aa-audit {{프로파일_이름}}`

- 여러 프로파일을 audit 모드로 설정:

`sudo aa-audit {{프로파일1 프로파일2 ...}}`

- 특정 디렉터리의 프로파일을 audit 모드로 설정:

`sudo aa-audit {{[-d|--dir]}} /{{경로/대상/프로파일}} {{프로파일_이름}}`

- 이미 적용된 경우에도 강제로 audit 모드로 설정:

`sudo aa-audit --force {{프로파일_이름}}`

- 프로파일을 재로드하지 않고 audit 모드 설정:

`sudo aa-audit --no-reload {{프로파일_이름}}`

- 프로파일의 audit 모드 해제:

`sudo aa-audit {{[-r|--remove]}} {{프로파일_이름}}`

- 도움말 표시:

`aa-audit {{[-h|--help]}}`
