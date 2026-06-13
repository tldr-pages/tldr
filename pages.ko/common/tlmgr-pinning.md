# tlmgr pinning

> 고정 작업은 고정 파일을 관리합니다.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#pinning>.

- 현재 고정 데이터를 표시:

`tlmgr pinning show`

- 일치하는 패키지를 주어진 저장소에 고정:

`tlmgr pinning add {{저장소}} {{패키지1 패키지2 ...}}`

- 주어진 저장소에 대해 고정 파일에 기록된 패키지를 제거:

`tlmgr pinning remove {{저장소}} {{패키지1 패키지2 ...}}`

- 주어진 저장소의 모든 고정 데이터 제거:

`tlmgr pinning remove {{저장소}} --all`
