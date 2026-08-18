# fmtutil-user

> 현재 사용자의 TeX 포맷과 Metafont 베이스를 관리.
> 더 많은 정보: <https://manned.org/fmtutil-sys>.

- 모든 사용자 포맷 파일 다시 생성:

`fmtutil-user --all`

- 누락된 모든 사용자 포맷 파일 다시 생성:

`fmtutil-user --missing`

- 지정한 사용자 포맷 다시 생성:

`fmtutil-user --byfmt {{포맷}}`

- 지정한 엔진으로 생성되는 모든 포맷 다시 생성:

`fmtutil-user --byengine {{엔진}}`

- 사용 가능한 모든 포맷 설정 목록 표시:

`fmtutil-user --listcfg`
