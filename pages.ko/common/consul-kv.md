# consul kv

> 서비스 검색 기능과 상태 확인을 위한 분산된 키-값(key-value)쌍 저장.
> 더 많은 정보: <https://learn.hashicorp.com/consul/getting-started/kv>.

- 키-값(key-value)쌍으로 저장된 값 읽기:

`consul kv get {{키}}`

- 새로운 키-값(key-value)쌍으로 저장:

`consul kv put {{키}} {{값}}`

- 키-값(key-value)쌍 제거:

`consul kv delete {{키}}`
