# pipwin

> Windows에서 비공식 Python 패키지 이진 파일을 설치하는 도구입니다.
> 더 많은 정보: <https://github.com/lepisma/pipwin>.

- 다운로드할 수 있는 모든 패키지 목록 표시:

`pipwin list`

- 패키지 검색:

`pipwin search {{일부_이름|이름}}`

- 패키지 설치:

`pipwin install {{패키지}}`

- 패키지 제거:

`pipwin uninstall {{패키지}}`

- 특정 디렉토리에 패키지 다운로드:

`pipwin download --dest {{경로\대상\디렉토리}} {{패키지}}`

- `requirements.txt`에 따라 패키지 설치:

`pipwin install --file {{경로\대상\requirements.txt}}`
