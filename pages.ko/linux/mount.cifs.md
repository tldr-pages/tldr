# mount.cifs

> SMB (Server Message Block) 또는 CIFS (Common Internet File System) 공유를 마운트.
> 참고: `mount`에 `-t cifs` 옵션을 전달하여 동일한 작업을 수행할 수 있습니다.
> 더 많은 정보: <https://manned.org/mount.cifs>.

- 지정된 사용자명 또는 기본적으로 `$USER`를 사용하여 연결 (비밀번호 입력 필요):

`mount.cifs -o user={{사용자명}} //{{서버}}/{{공유_이름}} {{마운트_지점}}`

- 게스트 사용자로 연결 (비밀번호 없이):

`mount.cifs -o guest //{{서버}}/{{공유_이름}} {{마운트_지점}}`

- 마운트된 디렉토리의 소유권 정보 설정:

`mount.cifs -o uid={{사용자_ID|사용자명}},gid={{그룹_ID|그룹명}} //{{서버}}/{{공유_이름}} {{마운트_지점}}`
