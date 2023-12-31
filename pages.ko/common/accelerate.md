# Accelerate

> Accelerate는 동일한 PyTorch 코드를 모든 분산 환경 구성에서 실행할 수 있게 해주는 라이브러리입니다.
> 더 많은 정보: <https://huggingface.co/docs/accelerate/index>.

- 실행환경 정보 출력:

`accelerate env`

- 대화형으로 구성 파일 생성:

`accelerate config`

- 다양한 데이터 타입을 사용하여 Hugging Face 모델을 실행하는 데 필요한 예상 GPU 메모리 비용을 출력:

`accelerate estimate-memory {{이름/모델}}`

- Accelerate 구성 파일 테스트:

`accelerate test --config_file {{경로/대상/구성파일.yaml}}`

- Accelerate를 사용하여 CPU에서 모델을 실행:

`accelerate launch {{경로/대상/스크립트.py}} {{--cpu}}`

- 2대의 머신을 사용하고, Accelerate로 다중 GPU에서 모델을 실행:

`accelerate launch {{경로/대상/스크립트.py}} --multi_gpu --num_machines 2`
