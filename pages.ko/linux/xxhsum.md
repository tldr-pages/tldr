# xxhsum

> 빠른 비암호화 알고리즘인 xxHash를 사용하여 체크섬을 출력하거나 검증합니다.
> 더 많은 정보: <https://github.com/Cyan4973/xxHash>.

- 특정 알고리즘을 사용하여 [f]파일의 체크섬 계산:

`xxhsum -H{{0|32|64|128}} {{경로/대상/파일}}`

- 벤치마크 실행:

`xxhsum -b`
