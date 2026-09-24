# share

> 로컬 리소스/파일시스템을 원격 시스템에서 마운트할 수 있도록 공유하는 도구.
> 더 많은 정보: <https://docs.oracle.com/cd/E36784_01/html/E36825/gntjt.html>.

- 현재 공유된 모든 파일시스템 목록 출력:

`share`

- 읽기/쓰기 권한으로 디렉터리 공유:

`share -F nfs -o rw /{{경로/대상/디렉터리}}`

- 읽기 전용으로 디렉터리 공유:

`share -F nfs -o ro /{{경로/대상/디렉터리}}`

- 특정 옵션으로 디렉터리 공유 (예: 특정 호스트에서 root 접근 허용):

`share -F nfs -o rw,root={{호스트명}} /{{경로/대상/디렉터리}}`

- `/etc/dfs/dfstab`에 추가하여 영구적으로 공유 설정:

`echo "share -F nfs -o rw /{{경로/대상/디렉터리}}" >> /etc/dfs/dfstab`
