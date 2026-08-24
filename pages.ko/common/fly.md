# fly

> concourse-ci용 명령줄 도구.
> 더 많은 정보: <https://concourse-ci.org/fly.html>.

- concourse 대상으로 인증 및 저장:

`fly {{[-t|--target]}} {{타겟_이름}} login {{[-n|--team-name]}} {{팀_이름}} {{[-c|--concourse-url]}} {{https://ci.example.com}}`

- 타겟 나열:

`fly targets`

- 파이프라인 나열:

`fly {{[-t|--target]}} {{타겟_이름}} pipelines`

- 파이프라인 업로드 또는 업데이트:

`fly {{[-t|--target]}} {{타겟_이름}} set-pipeline {{[-c|--config]}} {{pipeline.yml}} {{[-p|--pipeline]}} {{파이프라인_이름}}`

- 파이프라인 일시중지 해제:

`fly {{[-t|--target]}} {{타겟_이름}} unpause-pipeline {{[-p|--pipeline]}} {{파이프라인_이름}}`

- 파이프라인 구성 표시:

`fly {{[-t|--target]}} {{타겟_이름}} get-pipeline {{[-p|--pipeline]}} {{파이프라인_이름}}`

- fly의 로컬 사본 업데이트:

`fly {{[-t|--target]}} {{타겟_이름}} sync`

- 파이프라인 삭제:

`fly {{[-t|--target]}} {{타겟_이름}} destroy-pipeline {{[-p|--pipeline]}} {{파이프라인_이름}}`
