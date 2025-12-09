# paccache

> `pacman` 캐시 정리 도구.
> 더 많은 정보: <https://manned.org/paccache>.

- `pacman` 캐시에서 가장 최근의 3개 버전을 제외한 모든 패키지 버전 제거:

`paccache -r`

- 유지할 패키지 버전 수 설정:

`paccache -rk {{버전_수}}`

- 시뮬레이션을 수행하고 삭제 후보 패키지 수 표시:

`paccache -d`

- 삭제 대신 후보 패키지를 특정 폴더로 이동:

`paccache -m {{경로/대상/폴더}}`
