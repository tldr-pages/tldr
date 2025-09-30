# enum4linux

> 원격 시스템에서 Windows 및 Samba 정보를 열거합니다.
> 더 많은 정보: <https://labs.portcullis.co.uk/tools/enum4linux/>.

- 모든 방법을 사용하여 열거 시도:

`enum4linux -a {{원격_호스트}}`

- 주어진 로그인 자격 증명을 사용하여 열거:

`enum4linux -u {{사용자_이름}} -p {{비밀번호}} {{원격_호스트}}`

- 특정 호스트에서 사용자명 나열:

`enum4linux -U {{원격_호스트}}`

- 공유 목록 나열:

`enum4linux -S {{원격_호스트}}`

- 운영 체제 정보 가져오기:

`enum4linux -o {{원격_호스트}}`
