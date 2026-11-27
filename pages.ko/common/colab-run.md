# colab run

> 새로운 Google Colab VM에서 Python 스크립트를 실행하고 완료 시 자동으로 VM 해제.
> 더 많은 정보: <https://github.com/googlecolab/google-colab-cli#execution>.

- 새로운 CPU VM에서 로컬 스크립트를 실행하고 완료 시 VM 해제:

`colab run {{경로/대상/스크립트.py}}`

- GPU 런타임에서 로컬 스크립트 실행:

`colab run --gpu {{T4|L4|G4|A100|H100}} {{경로/대상/스크립트.py}}`

- TPU 런타임에서 로컬 스크립트 실행:

`colab run --tpu {{v5e1|v6e1}} {{경로/대상/스크립트.py}}`

- 명령줄 인수를 전달하여 스크립트 실행:

`colab run {{경로/대상/스크립트.py}} {{인자1 인자2 ...}}`

- GPU에서 스크립트를 실행하고 완료 후에도 세션을 활성 상태로 유지:

`colab run --gpu {{T4|L4|G4|A100|H100}} --keep {{경로/대상/스크립트.py}}`

- 사용자 지정 타임아웃을 지정하여 명명된 세션에서 스크립트 실행:

`colab run {{[-s|--session]}} {{세션_이름}} --timeout {{60.0}} {{경로/대상/스크립트.py}}`
