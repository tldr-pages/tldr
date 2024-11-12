# fscrypt

> Linux 파일 시스템 암호화를 관리하는 Go 도구.
> 더 많은 정보: <https://github.com/google/fscrypt>.

- fscrypt를 사용하기 위해 루트 파일 시스템 준비:

`fscrypt setup`

- 디렉터리에 파일 시스템 암호화 활성화:

`fscrypt encrypt {{경로/대상/폴더}}`

- 암호화된 디렉터리 잠금 해제:

`fscrypt unlock {{경로/대상/암호화된_폴더}}`

- 암호화된 디렉터리 잠금:

`fscrypt lock {{경로/대상/암호화된_폴더}}`
