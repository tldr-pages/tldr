# apx pkgmanagers

> `apx`에서 패키지 관리자를 관리합니다.
> 참고: 사용자가 생성한 패키지 관리자 구성은 `~/.local/share/apx/pkgmanagers`에 저장됩니다.
> 더 많은 정보: <https://docs.vanillaos.org/docs/en/apx-manpage#pkgmanagers>.

- 새 패키지 관리자 구성을 대화형으로 생성:

`apx pkgmanagers create`

- 사용 가능한 모든 패키지 관리자 구성 나열:

`apx pkgmanagers list`

- 패키지 관리자 구성 제거:

`apx pkgmanagers rm --name {{문자열}}`

- 특정 패키지 관리자에 대한 정보 표시:

`apx pkgmanagers show {{이름}}`
