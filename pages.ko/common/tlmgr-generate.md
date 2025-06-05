# tlmgr generate

> 로컬에 저장된 정보를 바탕으로 구성 파일을 다시 생성.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#generate>.

- 특정 위치에 구성 파일 저장 후 다시 생성:

`tlmgr generate --dest {{출력_파일}}`

- 로컬 구성 파일을 사용하여 구성 파일 다시 생성:

`tlmgr generate --localcfg {{로컬_구성_파일}}`

- 구성 파일 재구성 후 필요한 프로그램 실행:

`tlmgr generate --rebuild-sys`
