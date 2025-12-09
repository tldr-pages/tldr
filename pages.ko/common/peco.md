# peco

> 인터랙티브 필터링 도구.
> 더 많은 정보: <https://github.com/peco/peco>.

- 지정된 디렉터리의 모든 파일에서 `peco` 시작:

`find {{경로/대상/폴더}} -type f | peco`

- 실행 중인 프로세스에서 `peco` 시작:

`ps aux | peco`

- 지정된 쿼리와 함께 `peco` 시작:

`peco --query "{{쿼리}}"`
