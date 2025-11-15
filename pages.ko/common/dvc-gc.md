# dvc gc

> 캐시 또는 원격 저장소에서 사용되지 않는 파일 및 디렉토리를 제거.
> 더 많은 정보: <https://dvc.org/doc/command-reference/gc>.

- 현재 작업 공간에서 참조하는 버전만 남기고 캐시에서 가비지 수집:

`dvc gc --workspace`

- 브랜치, 태그, 커밋에서 참조하는 버전만 남기고 캐시에서 가비지 수집:

`dvc gc --all-branches --all-tags --all-commits`

- 기본 클라우드 원격 저장소를 포함하여 캐시에서 가비지 수집 (설정된 경우):

`dvc gc --all-commits --cloud`

- 특정 클라우드 원격 저장소를 포함하여 캐시에서 가비지 수집:

`dvc gc --all-commits --cloud --remote {{원격_이름}}`
