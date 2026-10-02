# sync

> 대기 중인 모든 쓰기 작업을 적절한 디스크에 반영.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>.

- 모든 디스크의 대기 중인 쓰기 작업 반영:

`sync`

- 지정한 파일의 대기 중인 쓰기 작업을 디스크에 반영:

`sync {{경로/대상/파일}}`

- 쓰기 작업을 디스크에 반영하고 파일 시스템 캐시 비우기:

`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`
