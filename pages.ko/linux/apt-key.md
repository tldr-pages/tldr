# apt-key

> Debian 및 Ubuntu의 APT 패키지 관리자를 위한 키 관리 도구.
> 참고: `apt-key`는 이제 더 이상 사용되지 않습니다 (`apt-key del`의 유지 보수 스크립트에서의 사용 제외).
> 더 많은 정보: <https://manned.org/apt-key.8>.

- 신뢰할 수 있는 키 나열:

`apt-key list`

- 신뢰할 수 있는 키 저장소에 키 추가:

`apt-key add {{공개_키_파일.asc}}`

- 신뢰할 수 있는 키 저장소에서 키 삭제:

`apt-key del {{키_ID}}`

- 원격 키를 신뢰할 수 있는 키 저장소에 추가:

`wget {{[-qO|--quiet --output-document]}} - {{https://host.tld/filename.key}} | apt-key add -`

- 키 ID만 사용하여 키서버에서 키 추가:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
