# setfattr

> 확장 파일 속성 설정.
> 더 많은 정보: <https://manned.org/setfattr>.

- 파일의 속성 이름 설정:

`setfattr -n user.{{속성_이름}} {{경로/대상/파일}}`

- 파일의 사용자 정의 확장 속성 값 설정:

`setfattr -n user.{{속성_이름}} -v "{{값}}" {{경로/대상/파일}}`

- 파일의 특정 속성 제거:

`setfattr -x user.{{속성_이름}} {{경로/대상/파일}}`
