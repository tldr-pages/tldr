# litert-lm

> LiteRT-LM 모델 실행 및 관리.
> 더 많은 정보: <https://developers.google.com/edge/litert-lm/cli/usage>.

- 가져온 모든 모델 목록 표시:

`litert-lm list`

- 로컬 또는 가져온 모델을 대화형으로 실행:

`litert-lm run {{경로/대상/모델.litertlm|model_id}}`

- Hugging Face 저장소에서 모델을 직접 불러와 단일 프롬프트 실행:

`litert-lm run --from-huggingface-repo {{소유자/저장소}} {{model.litertlm}} --prompt "{{What is the capital of France?}}"`

- GPU 가속을 사용하여 모델을 실행:

`litert-lm run {{경로/대상/모델.litertlm|model_id}} --backend gpu`

- 이미지를 첨부하여 멀티모달 모델 실행:

`litert-lm run {{경로/대상/모델.litertlm|model_id}} --vision-backend {{gpu|cpu}} --attachment {{경로/대상/이미지.jpg}} --prompt "{{Describe this image.}}"`

- preset 파일을 통해 Python 함수 호출 도구와 함께 모델 실행:

`litert-lm run {{경로/대상/모델.litertlm|model_id}} --preset {{경로/대상/preset.py}}`

- 모델 성능 벤치마크 실행:

`litert-lm benchmark {{경로/대상/모델.litertlm|model_id}}`

- 지정한 포트에서 OpenAI 호환 API 서버 시작:

`litert-lm serve --port {{9379}}`
