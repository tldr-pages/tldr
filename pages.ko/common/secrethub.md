# secrethub

> 구성 파일에서 비밀을 분리합니다.
> 더 많은 정보: <https://github.com/secrethub/secrethub-cli>.

- 비밀을 `stdout`에 출력:

`secrethub read {{경로/대상/비밀}}`

- 무작위 값을 생성하여 새 비밀로 저장하거나 업데이트:

`secrethub generate {{경로/대상/비밀}}`

- 클립보드의 값을 새 비밀로 저장하거나 업데이트:

`secrethub write --clip {{경로/대상/비밀}}`

- `stdin`에서 제공된 값을 새 비밀로 저장하거나 업데이트:

`echo "{{비밀_값}}" | secrethub write {{경로/대상/비밀}}`

- 저장소 또는 비밀 감사:

`secrethub audit {{경로/대상/저장소_또는_비밀}}`
