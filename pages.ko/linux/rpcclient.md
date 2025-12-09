# rpcclient

> MS-RPC 클라이언트 도구 (samba 모음의 일부).
> 더 많은 정보: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>.

- 원격 호스트에 연결:

`rpcclient --user {{도메인}}\{{사용자명}}%{{비밀번호}} {{IP}}`

- 비밀번호 없이 도메인에 있는 원격 호스트에 연결:

`rpcclient --user {{사용자명}} --workgroup {{도메인}} --no-pass {{IP}}`

- 비밀번호 해시를 전달하여 원격 호스트에 연결:

`rpcclient --user {{도메인}}\{{사용자명}} --pw-nt-hash {{IP}}`

- 원격 호스트에서 셸 명령 실행:

`rpcclient --user {{도메인}}\{{사용자명}}%{{비밀번호}} --command {{세미콜론_구분_명령들}} {{IP}}`

- 도메인 사용자 표시:

`rpcclient $> enumdomusers`

- 권한 표시:

`rpcclient $> enumprivs`

- 특정 사용자에 대한 정보 표시:

`rpcclient $> queryuser {{사용자명|RID}}`

- 도메인에 새 사용자 생성:

`rpcclient $> createdomuser {{사용자명}}`
