# mkisofs

> 디렉터리에서 ISO 파일 생성.
> `genisoimage`라는 별칭으로도 사용됩니다.
> 더 많은 정보: <https://manned.org/mkisofs>.

- 디렉터리에서 ISO 생성:

`mkisofs -o {{파일명.iso}} {{경로/대상/소스_디렉터리}}`

- ISO 생성 시 디스크 레이블 설정:

`mkisofs -o {{파일명.iso}} -V "{{레이블_이름}}" {{경로/대상/소스_디렉터리}}`
