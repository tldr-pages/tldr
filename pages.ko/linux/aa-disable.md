# aa-disable

> AppArmor 보안 정책 비활성화.
> 같이 보기: `aa-complain`, `aa-enforce`, `aa-status`.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- 프로필 비활성화:

`sudo aa-disable {{경로/대상/프로필1 경로/대상/프로필2 ...}}`

- 디렉토리 내의 프로필 비활성화 (기본값은 `/etc/apparmor.d`):

`sudo aa-disable --dir {{경로/대상/프로필들}}`
