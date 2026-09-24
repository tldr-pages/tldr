# aa-cleanprof

> 사용되지 않는 규칙을 제거하여 AppArmor 보안 프로파일을 정리하는 도구.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-cleanprof.8>.

- 프로파일에서 사용되지 않는 규칙 제거:

`sudo aa-cleanprof {{프로파일_이름}}`

- 여러 프로파일을 한 번에 정리:

`sudo aa-cleanprof {{프로파일1 프로파일2 ...}}`

- 프로파일이 있는 디렉터리 지정:

`sudo aa-cleanprof {{[-d|--dir]}} /{{경로/대상/프로파일}} {{프로파일_이름}}`

- 프롬프트 없이 조용히 실행:

`sudo aa-cleanprof {{[-s|--silent]}} {{프로파일_이름}}`

- 정리 후 프로파일 재로드 방지:

`sudo aa-cleanprof --no-reload {{프로파일_이름}}`

- 도움말 표시:

`aa-cleanprof {{[-h|--help]}}`
