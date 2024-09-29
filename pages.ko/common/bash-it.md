# bash-it

> 커뮤니티에서 제공한 Bash 3.2+용 Bash 명령 및 스크립트 모음.
> 더 많은 정보: <https://bash-it.readthedocs.io/en/latest/>.

- Bash-it을 최신 안정/개발 버전으로 업데이트:

`bash-it update {{stable|dev}}`

- Bash 프로필 다시 로드 (자동 다시 로드를 위해 `BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE`를 비어있지 않은 값으로 설정):

`bash-it reload`

- Bash 재시작:

`bash-it restart`

- 오류 및 경고 로깅이 활성화된 Bash 프로필을 다시 로드:

`bash-it doctor`

- 오류/경고/전체 로깅이 활성화된 Bash 프로필을 다시 로드:

`bash-it doctor {{errors|warnings|all}}`

- Bash-it 별칭/플러그인/완성 검색:

`bash-it search {{alias|plugin|completion}}`

- Bash-it 별칭/플러그인/완성을 검색하고 발견된 모든 항목을 활성화/비활성화:

`bash-it search --{{enable|disable}} {{alias|plugin|completion}}`
