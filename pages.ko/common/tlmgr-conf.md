# tlmgr conf

> TeX Live 구성 관리.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#conf>.

- 현재 TeX Live 구성 보기:

`tlmgr conf`

- 현재 `texmf`, `tlmgr`, 또는 `updmap` 구성 보기:

`tlmgr conf {{texmf|tlmgr|updmap}}`

- 특정 구성 옵션만 보기:

`tlmgr conf {{texmf|tlmgr|updmap}} {{구성_키}}`

- 특정 구성 옵션 설정:

`tlmgr conf {{texmf|tlmgr|updmap}} {{구성_키}} {{값}}`

- 특정 구성 옵션 삭제:

`tlmgr conf {{texmf|tlmgr|updmap}} --delete {{구성_키}}`

- `\write18`을 통한 시스템 호출 실행 비활성화:

`tlmgr conf texmf {{shell_escape}} {{0}}`

- 모든 추가 `texmf` 트리 보기:

`tlmgr conf auxtrees show`
