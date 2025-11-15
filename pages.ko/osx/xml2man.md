# xml2man

> MPGL을 mdoc으로 컴파일합니다.
> 더 많은 정보: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

- MPGL 파일을 보기 가능한 man 페이지로 컴파일:

`xml2man {{경로/대상/명령_파일.mxml}}`

- MPGL 파일을 특정 출력 파일로 컴파일:

`xml2man {{경로/대상/서비스_파일.mxml}} {{경로/대상/서비스_파일.7}}`

- MPGL 파일을 특정 출력 파일로 컴파일하고, 파일이 이미 존재하면 덮어쓰기:

`xml2man -f {{경로/대상/함수_파일.mxml}} {{경로/대상/함수_파일.3}}`
