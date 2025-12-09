# showmount

> NFS 파일 시스템에 대한 정보를 표시합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/showmount>.

- 내보낸 모든 파일 시스템을 표시:

`showmount -e`

- 모든 NFS 클라이언트와 마운트된 디렉터리를 표시:

`showmount -a`

- NFS로 마운트된 모든 디렉터리 표시:

`showmount -d`

- 원격 서버에 대해 내보낸 모든 파일 시스템을 표시:

`showmount -e {{서버_주소}}`
