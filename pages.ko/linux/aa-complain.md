# aa-complain

> AppArmor 정책을 컴플레인 모드로 설정합니다.
> 같이 보기: `aa-disable`, `aa-enforce`, `aa-status`.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- 정책을 컴플레인 모드로 설정:

`sudo aa-complain {{경로/대상/프로필1 경로/대상/프로필2 ...}}`

- 정책들을 컴플레인 모드로 설정:

`sudo aa-complain --dir {{경로/대상/프로필들}}`
