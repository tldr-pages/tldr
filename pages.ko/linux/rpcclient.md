# rpcclient

> MS-RPC 클라이언트 도구 (samba 모음의 일부).
> 더 많은 정보: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>.

- 원격 호스트에 연결:

`rpcclient {{[-U|--user]}} {{도메인}}\{{사용자명}}%{{비밀번호}} {{ip}}`

- 비밀번호 없이 도메인에 있는 원격 호스트에 연결:

`rpcclient {{[-U|--user]}} {{사용자명}} {{[-W|--workgroup]}} {{도메인}} {{[-N|--no-pass]}} {{ip}}`

- 비밀번호 해시를 전달하여 원격 호스트에 연결:

`rpcclient {{[-U|--user]}} {{도메인}}\{{사용자명}} --pw-nt-hash {{ip}}`

- 원격 호스트에서 셸 명령 실행:

`rpcclient {{[-U|--user]}} {{도메인}}\{{사용자명}}%{{비밀번호}} {{[-c|--command]}} {{세미콜론_구분_명령들}} {{ip}}`

- 도메인 사용자 표시:

`enumdomusers`

- 권한 표시:

`enumprivs`

- 특정 사용자에 대한 정보 표시:

`queryuser {{사용자명|rid}}`

- 도메인에 새 사용자 생성:

`createdomuser {{사용자명}}`
