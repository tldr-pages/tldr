# portageq

> Gentoo Linux 패키지 관리자, Portage에 대한 정보를 조회합니다.
> 조회 가능한 Portage 전용 환경 변수가 `/var/db/repos/gentoo/profiles/info_vars`에 나열되어 있습니다.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Portageq>.

- Portage 전용 환경 변수의 값을 표시:

`portageq envvar {{변수}}`

- Portage로 구성된 저장소의 상세 목록 표시:

`portageq repos_config /`

- 우선순위에 따라 정렬된 저장소 목록 표시 (가장 높은 것부터):

`portageq get_repos /`

- 특정 원자(즉, 버전을 포함한 패키지 이름)에 대한 메타데이터 표시:

`portageq metadata / {{ebuild|porttree|binary|...}} {{카테고리}}/{{패키지}} {{BDEPEND|DEFINED_PHASES|DEPEND|...}}`
