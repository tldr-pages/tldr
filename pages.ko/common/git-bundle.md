# git bundle

> 객체와 참조를 아카이브로 패키징합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-bundle>.

- 특정 브랜치의 모든 객체와 참조를 포함하는 번들 파일 생성:

`git bundle create {{경로/대상/파일.bundle}} {{브랜치_이름}}`

- 모든 브랜치의 번들 파일 생성:

`git bundle create {{경로/대상/파일.bundle}} --all`

- 현재 브랜치의 마지막 5개의 커밋을 포함하는 번들 파일 생성:

`git bundle create {{경로/대상/파일.bundle}} -5 {{HEAD}}`

- 최근 7일간의 커밋을 포함하는 번들 파일 생성:

`git bundle create {{경로/대상/파일.bundle}} --since 7.days {{HEAD}}`

- 번들 파일이 유효하고 현재 저장소에 적용될 수 있는지 확인:

`git bundle verify {{경로/대상/파일.bundle}}`

- 번들에 포함된 참조 목록을 `stdout`에 출력:

`git bundle unbundle {{경로/대상/파일.bundle}}`

- 번들 파일에서 특정 브랜치를 현재 저장소로 언번들:

`git pull {{경로/대상/파일.bundle}} {{브랜치_이름}}`

- 번들에서 새 저장소 생성:

`git clone {{경로/대상/파일.bundle}}`
