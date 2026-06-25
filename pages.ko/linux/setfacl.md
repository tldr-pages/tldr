# setfacl

> 파일 접근 제어 목록(ACL) 설정.
> 더 많은 정보: <https://manned.org/setfacl>.

- [u]사용자에게 읽기 및 쓰기 권한으로 파일의 ACL [m]수정:

`setfacl {{[-m|--modify]}} u:{{사용자명}}:rw {{경로/대상/파일_또는_폴더}}`

- 모든 사용자에 대한 파일의 기본 ACL [m]수정:

`setfacl {{[-d|--default]}} {{[-m|--modify]}} u::rw {{경로/대상/파일_또는_폴더}}`

- 파일의 사용자에 대한 ACL 제거:

`setfacl {{[-x|--remove]}} u:{{사용자명}} {{경로/대상/파일_또는_폴더}}`

- 파일의 모든 ACL 항목 제거:

`setfacl {{[-b|--remove-all]}} {{경로/대상/파일_또는_폴더}}`
