# transmission-edit

> 토렌트 파일에서 announce URL을 수정.
> 같이 보기: `transmission`.
> 더 많은 정보: <https://manned.org/transmission-edit>.

- 토렌트의 announce 목록에 URL 추가 또는 삭제:

`transmission-edit --{{add|delete}} {{http://example.com}} {{경로/대상/파일.torrent}}`

- 토렌트 파일에서 트래커의 패스코드 업데이트:

`transmission-edit --replace {{기존-패스코드}} {{새로운-패스코드}} {{경로/대상/파일.torrent}}`
