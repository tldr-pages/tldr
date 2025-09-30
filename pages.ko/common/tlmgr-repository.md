# tlmgr repository

> TeX Live 설치의 저장소를 관리합니다.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#repository>.

- 모든 설정된 저장소와 해당 태그(설정된 경우)를 나열:

`tlmgr repository list`

- 특정 저장소에서 사용할 수 있는 모든 패키지를 나열:

`tlmgr repository list {{경로|url|태그}}`

- 특정 태그와 함께 새 저장소 추가 (태그는 필수 아님):

`sudo tlmgr repository add {{경로|url}} {{태그}}`

- 특정 저장소 제거:

`sudo tlmgr repository remove {{경로|url|태그}}`

- 새로운 저장소 목록 설정, 이전 목록 덮어쓰기:

`sudo tlmgr repository set {{경로|url|태그}}#{{태그}} {{경로|url|태그}}#{{태그}} {{...}}`

- 모든 설정된 저장소의 검증 상태 표시:

`tlmgr repository status`
