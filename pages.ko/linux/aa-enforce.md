# aa-enforce

> AppArmor 프로파일을 강제 모드로 설정합니다.
> 같이 보기: `aa-complain`, `aa-disable`, `aa-status`.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- 프로파일 활성화:

`sudo aa-enforce --dir {{경로/대상/프로파일}}`

- 여러 프로파일 활성화:

`sudo aa-enforce {{경로/대상/프로파일1 경로/대상/프로파일2 ...}}`
