# ollama

> 대규모 언어 모델 실행기.
> 사용 가능한 모델 목록은 <https://ollama.com/library>를 참조하세요.
> 더 많은 정보: <https://github.com/ollama/ollama>.

- 다른 명령을 실행하는 데 필요한 데몬 시작:

`ollama serve`

- 모델을 실행하고 대화:

`ollama run {{모델}}`

- 단일 프롬프트로 모델 실행:

`ollama run {{모델}} {{프롬프트}}`

- 다운로드된 모델 나열:

`ollama {{[ls|list]}}`

- 특정 모델 가져오기/업데이트:

`ollama pull {{모델}}`

- 실행 중인 모델 나열:

`ollama ps`

- 모델 삭제:

`ollama rm {{모델}}`

- `Modelfile`로부터 모델 생성:

`ollama create {{새_모델_이름}} {{[-f|--file]}} {{경로/대상/Modelfile}}`
