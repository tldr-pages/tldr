# wlc

> Weblate 인스턴스의 현지화 프로젝트를 관리.
> 더 많은 정보: <https://docs.weblate.org/en/latest/wlc.html#commands>.

- 설정 파일을 사용하여 프로젝트 목록 표시:

`wlc {{[-c|--config]}} {{경로/대상/파일}} list-projects`

- API URL과 API 키를 직접 지정하여 프로젝트의 컴포넌트 목록 표시:

`wlc {{[-u|--url]}} {{url}} {{[-k|--key]}} {{키}} ls {{프로젝트}}`

- 지정한 형식으로 컴포넌트의 번역 목록 표시:

`wlc {{[-f|--format]}} {{text|csv|json|html}} ls {{프로젝트}}/{{컴포넌트}}`

- 프로젝트 통계 출력:

`wlc stats {{프로젝트}}`

- 도움말 표시:

`wlc {{[-h|--help]}}`
