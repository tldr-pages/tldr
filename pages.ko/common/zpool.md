# zpool

> ZFS 풀 관리.
> 더 많은 정보: <https://manned.org/zpool>.

- 모든 ZFS 풀의 구성 및 상태 표시:

`zpool status`

- ZFS 풀에서 오류 검사 (모든 블록의 체크섬 검증). 매우 높은 CPU 및 디스크 사용량:

`zpool scrub {{풀_이름}}`

- 가져올 수 있는 ZFS 풀 목록:

`zpool import`

- ZFS 풀 가져오기:

`zpool import {{풀_이름}}`

- ZFS 풀 내보내기 (모든 파일 시스템 마운트 해제):

`zpool export {{풀_이름}}`

- 모든 풀 작업의 기록 표시:

`zpool history {{풀_이름}}`

- 미러링된 풀 생성:

`zpool create {{풀_이름}} mirror {{디스크1}} {{디스크2}} mirror {{디스크3}} {{디스크4}}`

- ZFS 풀에 캐시 (L2ARC) 장치 추가:

`zpool add {{풀_이름}} cache {{캐시_디스크}}`
