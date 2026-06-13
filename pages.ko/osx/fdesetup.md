# fdesetup

> FileVault 관련 정보를 설정하고 검색합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/fdesetup.8.html>.

- 현재 FileVault 활성화된 사용자 목록 표시:

`sudo fdesetup list`

- 현재 FileVault 상태 가져오기:

`fdesetup status`

- FileVault 활성화 사용자 추가:

`sudo fdesetup add -usertoadd {{사용자1}}`

- FileVault 활성화:

`sudo fdesetup enable`

- FileVault 비활성화:

`sudo fdesetup disable`
