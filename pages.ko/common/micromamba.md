# micromamba

> `conda` 패키지용 빠르고, 가벼우며, 독립형 패키지 및 환경 관리자.
> `conda`의 대체품으로 사용할 수 있으며, CI, Docker 및 경량 환경에 적합.
> 더 많은 정보: <https://manned.org/micromamba>.

- 특정 경로에 새로운 환경 생성 후 패키지 설치:

`micromamba create {{[-p|--prefix]}} /{{경로/대상/환경변수}} {{python=3.11 numpy}}`

- 이름 또는 경로로 환경 활성화:

`micromamba activate {{[-p|--prefix]}} /{{경로/대상/환경변수}}`

- 쉘에서 활성화하지 않고 환경 내부에서 명령어 실행:

`micromamba run {{[-p|--prefix]}} /{{경로/대상/환경변수}} {{pytest tests/}}`

- 현재 활성화된 환경에 패키지 설치:

`micromamba install {{scipy pandas}}`

- 현재 환경의 설치된 패키지 목록 조회:

`micromamba list`

- 채널 또는 현재 환경에서 패키지를 검색:

`micromamba search {{패키지_이름}}`

- 패키지 의존성 트리 조회:

`micromamba repoquery depends {{[-t|--tree]}} {{패키지_이름}}`

- 현재 `micromamba` 설정 정보 확인:

`micromamba info`
