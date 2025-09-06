# quotacheck

> 파일 시스템의 디스크 사용량을 스캔하여 쿼터 파일을 생성, 확인 및 복구합니다.
> 쿼터 파일의 손상이나 손실을 방지하기 위해 쿼터를 비활성화한 상태에서 실행하는 것이 좋습니다.
> 더 많은 정보: <https://manned.org/quotacheck>.

- 모든 마운트된 비-NFS 파일 시스템의 쿼터 확인:

`sudo quotacheck --all`

- 쿼터가 활성화된 상태에서도 강제 확인 (쿼터 파일의 손상이나 손실이 발생할 수 있음):

`sudo quotacheck --force {{마운트_지점}}`

- 디버그 모드로 주어진 파일 시스템의 쿼터 확인:

`sudo quotacheck --debug {{마운트_지점}}`

- 진행 상황을 표시하며 주어진 파일 시스템의 쿼터 확인:

`sudo quotacheck --verbose {{마운트_지점}}`

- 사용자 쿼터 확인:

`sudo quotacheck --user {{사용자}} {{마운트_지점}}`

- 그룹 쿼터 확인:

`sudo quotacheck --group {{그룹}} {{마운트_지점}}`
