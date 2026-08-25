# dnf download

> DNF 저장소에서 RPM 패키지 다운로드.
> 기본 `dnf` 명령에는 포함되지 않으며, `dnf-plugins-core`을 통해 지원됨.
> 관련 항목: `dnf`.
> 더 많은 정보: <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>.

- 최신 버전의 패키지를 현재 디렉터리에 다운로드:

`dnf download {{패키지}}`

- 지정한 디렉터리에 패키지 다운로드 (디렉터리는 미리 존재해야 합니다):

`dnf download {{패키지}} --destdir {{경로/대상/디렉터리}}`

- RPM 패키지를 다운로드할 수 있는 URL 출력:

`dnf download --url {{패키지}}`
