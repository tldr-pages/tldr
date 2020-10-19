# bw

> Bitwarden 보관함에 접속과 관리를 위한 CLI.
> 더 많은 정보: <https://help.bitwarden.com/article/cli/>.

- Bitwarden 사용자 계정 로그인:

`bw login`

- 사용자 계정 로그아웃:

`bw logout`

- Bitwarden 보관함으로부터 아이템 검색과 출력:

`bw list items --search {{github}}`

- Bitwarden 보관함으로부터 특정 아이템 출력:

`bw get item {{github}}`

- Bitwarden 보관함에 폴더 생성:

`{{echo -n '{"name":"My Folder1"}' | base64}} | bw create folder`
