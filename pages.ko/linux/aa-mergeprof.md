# aa-mergeprof

> AppArmor 보안 프로파일 파일을 프로파일 디렉터리에 병합하는 도구.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-mergeprof.8>.

- 하나 이상의 프로파일 파일을 기본 프로파일 디렉터리에 병합:

`sudo aa-mergeprof {{파일1 파일2 ...}}`

- 특정 디렉터리에 프로파일 파일 병합:

`sudo aa-mergeprof {{[-d|--dir]}} /{{path/to/profiles}} {{파일1 파일2 ...}}`

- 도움말 표시:

`aa-mergeprof {{[-h|--help]}}`
