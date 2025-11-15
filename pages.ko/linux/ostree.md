# ostree

> 운영 체제 루트 파일 시스템에 최적화된 바이너리 파일의 버전 관리 도구로, `git`과 유사합니다.
> OSTree는 Fedora Silverblue, Fedora IoT, Fedora CoreOS와 같은 불변 이미지 기반 운영 체제의 기초입니다.
> 더 많은 정보: <https://ostreedev.github.io/ostree>.

- `$PWD`의 파일을 `$PWD/path/to/repo`의 메타데이터와 함께 저장소로 초기화:

`ostree init --repo {{경로/대상/저장소}}`

- 파일의 커밋(스냅샷) 생성:

`ostree commit --repo {{경로/대상/저장소}} --branch {{브랜치_이름}}`

- 커밋 내 파일 표시:

`ostree ls --repo {{경로/대상/저장소}} {{커밋_ID}}`

- 커밋의 메타데이터 표시:

`ostree show --repo {{경로/대상/저장소}} {{커밋_ID}}`

- 커밋 목록 표시:

`ostree log --repo {{경로/대상/저장소}} {{브랜치_이름}}`

- 저장소 요약 표시:

`ostree summary --repo {{경로/대상/저장소}} --view`

- 사용 가능한 참조(브랜치) 표시:

`ostree refs --repo {{경로/대상/저장소}}`
