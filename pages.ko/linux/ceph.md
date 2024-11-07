# ceph

> 통합 스토리지 시스템.
> 더 많은 정보: <https://ceph.io/en>.

- 클러스터 상태 확인:

`ceph status`

- 클러스터 사용 통계 확인:

`ceph df`

- 클러스터 내 배치 그룹의 통계 가져오기:

`ceph pg dump --format {{plain}}`

- 스토리지 풀 생성:

`ceph osd pool create {{풀_이름}} {{페이지_번호}}`

- 스토리지 풀 삭제:

`ceph osd pool delete {{풀_이름}}`

- 스토리지 풀 이름 변경:

`ceph osd pool rename {{현재_이름}} {{새로운_이름}}`

- 풀 스토리지 자체 복구:

`ceph pg repair {{풀_이름}}`
