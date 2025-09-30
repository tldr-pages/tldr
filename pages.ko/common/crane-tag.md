# crane tag

> `copy` 명령과 달리 다운로드지 않고 원격 이미지에 효율적으로 태그를 지정.
> 매니페스트가 이미 존재한다는 것을 알고 있어, 레이어 존재 확인을 건너뛰므로 속도가 약간 빨라짐.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

- 원격 이미지 태깅:

`crane tag {{이미지_이름}} {{태그_이름}}`

- 도움말 표시:

`crane tag {{[-h|--help]}}`
