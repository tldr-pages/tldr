# getfattr

> 파일 이름 및 확장 속성을 표시합니다.
> 더 많은 정보: <https://manned.org/getfattr>.

- 파일의 모든 확장 속성을 가져와서 자세히 표시:

`getfattr -d {{경로/대상/파일}}`

- 파일의 특정 속성 가져오기:

`getfattr -n user.{{속성_이름}} {{경로/대상/파일}}`
