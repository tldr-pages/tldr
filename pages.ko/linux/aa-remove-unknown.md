# aa-remove-unknown

> 설정 디렉토리에 더 이상 존재하지 않는 AppArmor 프로파일을 제거하는 도구.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-remove-unknown.8>.

- 제거 대상 프로파일을 미리 확인:

`sudo aa-remove-unknown -n`

- 실제로 프로파일을 제거:

`sudo aa-remove-unknown`

- 도움말 표시:

`aa-remove-unknown {{[-h|--help]}}`
