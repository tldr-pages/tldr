# proctl

> 프로젝트 라이선스 및 언어를 관리하고, 템플릿화된 라이선스 간 전환을 수행합니다.
> 더 많은 정보: <https://github.com/HeCodes2Much/proctl>.

- 사용 가능한 라이선스 나열:

`proctl {{[-ll|-list-licenses]}}`

- 사용 가능한 언어 나열:

`proctl {{[-lL|-list-languages]}}`

- FZF 메뉴에서 라이선스 선택:

`proctl {{[-pl|-pick-license]}}`

- FZF 메뉴에서 언어 선택:

`proctl {{[-pL|-pick-language]}}`

- 현재 프로젝트에서 모든 라이선스 제거:

`proctl {{[-r|-remove-license]}}`

- 새 라이선스 템플릿 생성:

`proctl {{[-t|-new-template]}}`

- 템플릿에서 라이선스 삭제:

`proctl {{[-R|-delete-license]}} {{@라이선스_이름1 @라이선스_이름2 ...}}`

- 유용한 명령어 목록 표시:

`proctl {{[-h|-help]}}`
