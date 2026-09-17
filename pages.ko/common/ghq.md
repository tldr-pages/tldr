# ghq

> 호스트명과 경로 기준으로 원격 저장소 clone 관리.
> 더 많은 정보: <https://github.com/x-motemen/ghq>.

- 저장소를 `ghq` 루트 디렉터리 (기본값: `~/ghq`) 아래에 clone:

`ghq get {{저장소_주소}}`

- 사용자/프로젝트 형식으로 저장소 clone (기본값은 GitHub):

`ghq get {{사용자}}/{{프로젝트}}`

- 저장소를 clone한 뒤, 해당 디렉터리로 `cd` 사용해서 이동:

`ghq get {{저장소_주소}} --look`

- SSH를 사용하여 저장소 clone:

`ghq get {{사용자}}/{{프로젝트}} -p`

- 기존 저장소를 최신 버전으로 업데이트:

`ghq get {{저장소_주소}} -u`

- 로컬에 clone된 모든 저장소 목록 표시:

`ghq list`

- 전체 경로와 함께 로컬 저장소:

`ghq list --full-path`

- 로컬에 cloned 저장소 제거:

`ghq rm {{사용자}}/{{프로젝트}}`
