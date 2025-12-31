# yadm gitconfig

> `git config`에 옵션을 전달하여 `yadm`으로 관리하는 저장소의 `.gitconfig`를 변경합니다.
> 같이 보기: `git config`.
> 더 많은 정보: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>.

- Git 구성 값을 업데이트하거나 설정:

`yadm gitconfig {{키.내부키}} {{값}}`

- `yadm`의 Git 구성에서 값 가져오기:

`yadm gitconfig --get {{키}}`

- `yadm`의 Git 구성에서 값 제거:

`yadm gitconfig --unset {{키}}`

- `yadm`의 Git 구성의 모든 값 나열:

`yadm gitconfig --list`
