# raw

> Unix 원시 문자 장치를 블록 장치에 바인드합니다.
> 더 많은 정보: <https://manned.org/raw.8>.

- 원시 문자 장치를 블록 장치에 바인드:

`raw /dev/raw/raw{{1}} {{/dev/block_device}}`

- 새로운 바인딩을 설정하는 대신 기존 바인딩 조회:

`raw /dev/raw/raw{{1}}`

- 바인드된 모든 원시 장치 조회:

`raw -qa`
