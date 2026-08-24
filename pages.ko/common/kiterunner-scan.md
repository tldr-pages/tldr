# kiterunner scan

> kitebuilder 워드리스트를 사용하여 API 경로 및 웹 엔드포인트를 동시 스캔하는 컨텍스트 기반 웹 스캐너 .
> `scan` 하위 명령어는 구조화된 API 요청으로 하나 이상의 호스트를 대상으로 스캔 수행.
> 더 많은 정보: <https://github.com/assetnote/kiterunner#usage>.

- Assetnote 워드리스트 (예: 상위 5000개 API 경로)를 사용하여 대상 스캔:

`kiterunner scan {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210228:5000}}`

- kitebuilder 워드리스트를 사용하여 대상 스캔:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{경로/대상/워드리스트.kite}}`

- 파일에 정의된 여러 호스트를 kitebuilder 워드리스트로 스캔:

`kiterunner scan {{경로/대상/호스트.txt}} {{[-w|--kitebuilder-list]}} {{경로/대상/워드리스트.kite}}`

- Assetnote 워드리스트를 사용하고 결과를 JSON 형식으로 출력하며 스캔:

`kiterunner scan {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210228:5000}} -o {{json}}`

- 성능 향상을 위해 사용자 지정 동시성 설정으로 스캔:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{경로/대상/워드리스트.kite}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- 워드리스트를 일반 워드리스트처럼 사용하며, 깊이 스캔을 비활성화하여 스캔:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{경로/대상/rafter.txt}} {{[-d|--preflight-depth]}} {{0}}`

- 사용자 지정 헤더를 사용하고 특정 콘텐츠 길이 응답을 무시하며 스캔:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{경로/대상/워드리스트.kite}} {{[-H|--header]}} "{{Authorization: Bearer token}}" --ignore-length {{100-105}}`

- 단계별 스캔 없이 전체 kitebuilder 스캔 수행:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{경로/대상/워드리스트.kite}} --kitebuilder-full-scan`
