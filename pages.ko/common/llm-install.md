# llm install

> 플러그인을 추가하기 위해 LLM과 동일한 환경에 Python 패키지를 설치.
> 더 많은 정보: <https://llm.datasette.io/en/stable/help.html#llm-install-help>.

- PyPI에서 플러그인 설치:

`llm install {{플러그인_이름}}`

- 플러그인을 최신 버전으로 업그레이드:

`llm install {{[-U|--upgrade]}} {{플러그인_이름}}`

- 편집 가능(editable) 모드로 로컬 플러그인 설치:

`llm install {{[-e|--editable]}} {{경로/대상/플러그인_디렉터리}}`

- 이미 최신 상태인 경우에도 플러그인 재설치:

`llm install --force-reinstall {{플러그인_이름}}`

- 플러그인 설치 시 시험판(pre-release) 버전 포함:

`llm install --pre {{플러그인_이름}}`
