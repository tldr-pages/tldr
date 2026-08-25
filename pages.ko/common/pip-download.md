# pip download

> Python 패키지를 설치하지 않고 다운로드.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_download/>.

- 패키지 wheel 또는 소스 아카이브를 현재 디렉터리에 다운로드:

`pip download {{패키지}}`

- 특정 버전의 패키지 다운로드:

`pip download {{패키지}}=={{버전}}`

- 패키지와 의존성을 특정 디렉터리에 다운로드:

`pip download {{패키지}} {{[-d|--dest]}} {{경로/대상/디렉터리}}`

- 특정 플랫폼 및 Python 버전에 맞는 패키지 다운로드:

`pip download {{패키지}} --only-binary :all: --platform {{플랫폼}} --python-version {{버전}}`

- 특정 인덱스 URL로부터 패키지 다운로드:

`pip download {{패키지}} {{[-i|--index-url]}} {{주소}}`
