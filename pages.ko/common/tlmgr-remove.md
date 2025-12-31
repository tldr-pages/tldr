# tlmgr remove

> TeX Live 패키지 제거.
> 기본적으로, 제거된 패키지는 TL 설치 디렉토리의 `./tlpkg/backups`에 백업됩니다.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#remove-option...-pkg>.

- TeX Live 패키지 제거:

`sudo tlmgr remove {{패키지}}`

- 패키지를 실제로 제거하지 않고 시뮬레이션:

`tlmgr remove --dry-run {{패키지}}`

- 패키지의 의존성을 제외하고 제거:

`sudo tlmgr remove --no-depends {{패키지}}`

- 패키지를 특정 디렉토리에 백업하며 제거:

`sudo tlmgr remove --backupdir {{경로/대상/폴더}} {{패키지}}`

- TeX Live 전체를 제거하고 확인 요청:

`sudo tlmgr remove --all`
