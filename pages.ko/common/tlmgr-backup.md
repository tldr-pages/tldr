# tlmgr backup

> TeX Live 패키지의 백업을 관리.
> 기본 백업 디렉토리는 `backupdir` 옵션에 의해 지정되며, `tlmgr option`으로 확인 가능.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#backup>.

- 하나 이상의 패키지 백업:

`tlmgr backup {{패키지1 패키지2 ...}}`

- 모든 패키지 백업:

`tlmgr backup --all`

- 사용자 지정 디렉토리에 백업:

`tlmgr backup {{패키지}} --backupdir {{경로/대상/백업_디렉토리}}`

- 하나 이상의 패키지 백업 삭제:

`tlmgr backup clean {{패키지1 패키지2 ...}}`

- 모든 백업 삭제:

`tlmgr backup clean --all`
