# gitleaks

> Git 레포지토리에서 유출된 비밀 및 API 키를 탐지.
> 더 많은 정보: <https://github.com/gitleaks/gitleaks>.

- 원격 디렉터리 스캔:

`gitleaks detect --repo-url {{https://github.com/username/repository.git}}`

- 로컬 디렉터리 스캔:

`gitleaks detect --source {{경로/대상/디렉터리}}`

- 스캔 결과를 JSON 파일로 출력:

`gitleaks detect --source {{경로/대상/디렉터리}} --report {{경로/대상/리포트.json}}`

- 사용자 정의 규칙 파일을 사용:

`gitleaks detect --source {{경로/대상/디렉터리}} --config-path {{경로/대상/구성파일.toml}}`

- 특정 커밋에서 스캔을 시작:

`gitleaks detect --source {{경로/대상/디렉터리}} --log-opts {{--since=commit_id}}`

- 커밋 전에 커밋되지 않은 변경사항을 검색:

`gitleaks protect --staged`

- 스캔 중에 보안 위험 노출로 식별된 부분을 나타내는 자세한 출력을 표시:

`gitleaks protect --staged --verbose`
