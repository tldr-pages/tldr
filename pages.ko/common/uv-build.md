# uv build

> Python 패키지를 소스 배포판과 wheel로 빌드.
> 더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-build>.

- 현재 디렉터리의 패키지 빌드:

`uv build`

- 지정한 디렉터리의 패키지 빌드:

`uv build {{경로/대상/디렉터리}}`

- wheel만 빌드 (소스 배포판 제외):

`uv build --wheel`

- 소스 배포판만 빌드 (wheel 제외):

`uv build --sdist`

- 빌드 결과를 지정한 디렉터리에 출력:

`uv build {{[-o|--out-dir]}} {{경로/대상/출력파일}}`

- workspace에서 지정한 패키지 빌드:

`uv build --package {{패키지_이름}}`

- workspace의 모든 패키지 빌드:

`uv build {{[--all|--all-packages]}}`

- 지정한 Python 인터프리터를 사용해 빌드:

`uv build {{[-p|--python]}} {{python3.11}}`
