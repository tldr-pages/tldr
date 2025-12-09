# reflector

> Arch 스크립트로 미러리스트를 가져오고 정렬합니다.
> 더 많은 정보: <https://manned.org/reflector>.

- 모든 미러를 가져와 다운로드 속도로 정렬하고 저장:

`sudo reflector --sort {{rate}} --save {{/etc/pacman.d/mirrorlist}}`

- 독일의 HTTPS 미러만 가져오기:

`reflector --country {{Germany}} --protocol {{https}}`

- 최근에 동기화된 10개의 미러만 가져오기:

`reflector --latest {{10}}`
