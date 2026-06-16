# dnf reposync

> 원격 DNF 저장소의 패키지 및 메타데이터를 로컬 디렉터리와 동기화.
> 기본 `dnf` 명령에는 포함되지 않으며, `dnf-plugins-core`을 통해 지원됨.
> 관련 항목: `dnf`.
> 더 많은 정보: <https://dnf-plugins-core.readthedocs.io/en/latest/reposync.html>.

- 지정한 저장소 (`repo_name`)의 모든 패키지를 현재 작업 디렉터리의 `repo_name` 하위 디렉터리로 동기화:

`dnf reposync --repoid {{저장소_이름}}`

- 사용자 지정 저장 위치로 모든 패키지 동기화:

`dnf reposync --repoid {{저장소_이름}} {{[-p|--download-path]}} {{경로/대상/디렉터리}}`

- 모든 패키지와 메타데이터 동기화:

`dnf reposync --repoid {{저장소_이름}} --download-metadata`

- 저장소 별로 최신 패키지만 다운로드:

`dnf reposync --repoid {{저장소_이름}} {{[-n|--newest-only]}}`

- 실제 다운로드 없이 다운로드될 URL만 출력:

`dnf reposync --repoid {{저장소_이름}} {{[-u|--urls]}}`

- 다운로드된 파일의 타임스탬프를 원격 저장소와 동일하게 설정을 시도:

`dnf reposync --repoid {{저장소_이름}} --remote-time`
