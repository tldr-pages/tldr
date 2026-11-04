# tv

> 크로스 플랫폼에서 사용할 수 있는 빠르고, 확장 가능한 퍼지 검색 도구.
> "채널" (예: 파일, 환경 변수, git 저장소 등) 또는 `stdin` 입력을 사용할 수 있음.
> 더 많은 정보: <https://alexpasmantier.github.io/television/>.

- 기본 채널로 실행:

`tv`

- 지정한 채널 열기:

`tv {{files|env|git-repos|...}}`

- 사용 가능한 모든 채널 목록 표시:

`tv list-channels`

- `stdin`으로 전달된 항목에서 퍼지 검색으로 선택:

`{{명령어}} | tv`

- 각 항목의 실시간 미리보기를 표시하며 선택:

`{{명령어}} | tv --preview '{{preview_command}}'`

- 명령을 사용해 선택기 생성 (소스 + 미리보기):

`tv --source-command '{{소스_명령어}}' --preview-command '{{프리뷰_명령어}}' --preview-size {{70}}`

- 커뮤니티에서 관리하는 채널 업데이트 및 설치:

`tv update-channels`

- tldr 페이지 보기 (채널 업데이트를 먼저하고 `tldr`가 설치되어 있어야 함):

`tv tldr`
