# git mergetool

> 병합 충돌을 해결하기 위해 병합 충돌 해결 도구를 실행.
> 더 많은 정보: <https://git-scm.com/docs/git-mergetool>.

- 기본 병합 도구를 실행하여 충돌 해결:

`git mergetool`

- 유효한 병합 도구 나열:

`git mergetool --tool-help`

- 이름으로 식별된 병합 도구 실행:

`git mergetool --tool {{tool_name}}`

- 병합 도구를 실행하기 전에 각 호출마다 묻지 않음:

`git mergetool --no-prompt`

- GUI 병합 도구를 명시적으로 사용 (설정 변수 `merge.guitool` 참조):

`git mergetool --gui`

- 일반 병합 도구를 명시적으로 사용 (설정 변수 `merge.tool` 참조):

`git mergetool --no-gui`
