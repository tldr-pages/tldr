# transmission-create

> BitTorrent `.torrent` 파일 만들기.
> 같이 보기: `transmission`.
> 더 많은 정보: <https://manned.org/transmission-create>.

- 2048 KB를 조각 크기로 하여 토렌트 생성:

`transmission-create {{[-o|--outfile]}} {{경로/대상/example.torrent}} {{[-t|--tracker]}} {{트래커_발표_URL}} {{[-s|--piecesize]}} {{2048}} {{경로/대상/파일_또는_폴더}}`

- 2048 KB 조각 크기로 개인 토렌트 생성:

`transmission-create {{[-p|--private]}} {{[-o|--outfile]}} {{경로/대상/example.torrent}} {{[-t|--tracker]}} {{트래커_발표_URL}} {{[-s|--piecesize]}} {{2048}} {{경로/대상/파일_또는_폴더}}`

- 코멘트를 포함하여 토렌트 생성:

`transmission-create {{[-o|--outfile]}} {{경로/대상/example.torrent}} {{[-t|--tracker]}} {{트래커_URL1}} {{[-c|--comment]}} {{코멘트}} {{경로/대상/파일_또는_폴더}}`

- 여러 트래커를 포함하여 토렌트 생성:

`transmission-create {{[-o|--outfile]}} {{경로/대상/example.torrent}} {{[-t|--tracker]}} {{트래커_URL1}} {{[-t|--tracker]}} {{트래커_URL2}} {{경로/대상/파일_또는_폴더}}`

- 도움말 페이지 표시:

`transmission-create {{[-h|--help]}}`
