# dnf versionlock

> 패키지가 최신 버전으로 업데이트되지 않도록 보호.
> 기본 `dnf` 명령에는 포함되지 않으며, `dnf-plugins-core`을 통해 지원됨.
> 관련 항목: `dnf`.
> 더 많은 정보: <https://dnf-plugins-core.readthedocs.io/en/latest/versionlock.html>.

- 현재 versionlock 항목 목록 표시:

`dnf versionlock`

- 지정한 패키지와 일치하는 모든 사용 가능한 패키지에 versionlock 추가:

`dnf versionlock add {{패키지}}`

- 지정한 패키지와 일치하는 패키지를 versionlock 내 제외 대상으로 추가:

`dnf versionlock exclude {{패키지}}`

- 일치하는 versionlock 항목을 제거:

`dnf versionlock delete {{패키지}}`

- 모든 versionlock 항목 제거:

`dnf versionlock clear`
