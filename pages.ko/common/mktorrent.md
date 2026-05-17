# mktorrent

> BitTorrent 메타정보 파일 생성.
> 더 많은 정보: <https://manned.org/mktorrent>.

- 조각 크기를 2^21 KB로 설정하여 토렌트 생성:

`mktorrent {{[-a|--announce]}} {{트래커_발표_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{경로/대상/예시.torrent}} {{경로/대상/파일_또는_폴더}}`

- 조각 크기를 2^21 KB로 설정하여 개인 토렌트 생성:

`mktorrent {{[-p|--private]}} {{[-a|--announce]}} {{트래커_발표_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{경로/대상/예시.torrent}} {{경로/대상/파일_또는_폴더}}`

- 주석이 포함된 토렌트 생성:

`mktorrent {{[-c|--comment]}} "{{주석}}" {{[-a|--announce]}} {{트래커_발표_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{경로/대상/예시.torrent}} {{경로/대상/파일_또는_폴더}}`

- 여러 트래커가 포함된 토렌트 생성:

`mktorrent {{[-a|--announce]}} {{트래커_발표_url,트래커_발표_url_2}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{경로/대상/예시.torrent}} {{경로/대상/파일_또는_폴더}}`

- 웹 시드 URL이 포함된 토렌트 생성:

`mktorrent {{[-a|--announce]}} {{트래커_발표_url}} -w {{웹_시드_url}} {{[-l|--piece-length]}} {{21}} {{[-o|--output]}} {{경로/대상/예시.torrent}} {{경로/대상/파일_또는_폴더}}`
