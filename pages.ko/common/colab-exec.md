# colab exec

> 활성 Google Colab 세션에서 코드를 실행.
> 더 많은 정보: <https://github.com/googlecolab/google-colab-cli#execution>.

- `stdin`을 통해 전달된 코드 실행:

`echo "{{print('Hello from Colab')}}" | colab exec`

- 활성 세션에서 로컬 Python 스크립트 실행:

`colab exec {{[-f|--file]}} {{경로/대상/스크립트.py}}`

- 지정된 세션에서 로컬 Jupyter 노트북 실행:

`colab exec {{[-s|--session]}} {{세션_이름}} {{[-f|--file]}} {{경로/대상/노트북.ipynb}}`

- 스크립트를 실행하고 생성된 플롯을 이미지 파일로 저장:

`colab exec {{[-f|--file]}} {{경로/대상/스크립트.py}} --output-image {{경로/대상/플롯.png}}`

- 사용자 지정 제한 시간(초)을 설정하여 코드 실행:

`colab exec {{[-f|--file]}} {{경로/대상/스크립트.py}} --timeout {{60.0}}`
