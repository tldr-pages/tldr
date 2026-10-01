# uv self

> `uv` 실행 파일 자체를 관리.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-self>.

- `uv`를 최신 버전으로 업데이트:

`uv self update`

- `uv`를 지정한 버전으로 업데이트:

`uv self update {{0.4.0}}`

- 설치하지 않고 사용 가능한 `uv` 업데이트 확인:

`uv self update --dry-run`

- 자세한 출력을 표시하며 `uv` 업데이트:

`uv self update {{[-v|--verbose]}}`

- 현재 `uv` 버전 표시:

`uv self version`

- 버전 번호만 표시:

`uv self version --short`

- 버전 정보를 JSON 형식으로 표시:

`uv self version --output-format json`
