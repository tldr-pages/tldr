# yadm git-crypt

> Git Crypt는 Git 저장소에서 파일의 투명한 암호화 및 복호화를 가능하게 합니다.
> 같이 보기: `git-crypt`.
> 더 많은 정보: <https://github.com/AGWA/git-crypt>.

- Git Crypt를 사용하도록 저장소 초기화:

`yadm git-crypt init`

- GPG를 사용하여 저장소 공유:

`yadm git-crypt add-gpg-user {{사용자_아이디}}`

- 암호화된 파일이 있는 저장소를 복제한 후 파일 잠금 해제:

`yadm git-crypt unlock`

- 대칭 비밀 키 내보내기:

`yadm git-crypt export-key {{경로/대상/키_파일}}`
