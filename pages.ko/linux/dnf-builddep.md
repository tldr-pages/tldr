# dnf builddep

> 지정한 패키지를 빌드하기 위한 의존성 설치.
> 기본 `dnf` 명령에는 포함되지 않으며, `dnf-plugins-core`을 통해 지원됨.
> 관련 항목: `dnf`.
> 더 많은 정보: <https://dnf-plugins-core.readthedocs.io/en/latest/builddep.html>.

- 지정한 패키지의 빌드 의존성 설치:

`dnf builddep {{경로/대상/스펙파일.spec}}`

- 사용할 수 없는 의존성 무시하고 빌드 의존성 설치:

`dnf builddep --skip-unavailable {{경로/대상/스펙파일.spec}}`

- RPM 매크로를 지정한 표현식으로 정의:

`dnf builddep {{[-D|--define]}} '{{표현식}}'`

- `.spec` 파일 경로 인자 지정:

`dnf builddep --spec {{인자}}`

- `.rpm` 파일 경로 인자 지정:

`dnf builddep --srpm {{인자}}`

- 도움말 표시:

`dnf builddep --help-cmd`
