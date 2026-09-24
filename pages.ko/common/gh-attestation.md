# gh attestation

> 아티팩트 인증을 다운로드하고 검증하여 무결성 및 출처 확인.
> 더 많은 정보: <https://cli.github.com/manual/gh_attestation>.

- 특정 저장소와 연결된 로컬 파일의 인증 다운로드:

`gh {{[at|attestation]}} download {{경로/대상/아티팩트.bin}} {{[-R|--repo]}} {{소유자}}/{{저장소}}`

- 조직과 연결된 OCI 컨테이너 이미지의 인증 다운로드:

`gh {{[at|attestation]}} download oci://{{image_uri}} {{[-o|--owner]}} {{조직_이름}}`

- 특정 저장소의 인증을 사용해 로컬 아티팩트를 온라인 검증:

`gh {{[at|attestation]}} verify {{경로/대상/아티팩트.bin}} {{[-R|--repo]}} {{소유자}}/{{저장소}}`

- 보안 강화를 위해, 특정 재사용 가능한 워크플로우로 서명되었는지 요구하여 아티팩트 검증:

`gh {{[at|attestation]}} verify {{경로/대상/아티팩트.bin}} {{[-o|--owner]}} {{조직_이름}} --signer-workflow {{소유자}}/{{저장소}}/{{경로/대상/워크플로우.yml}}`

- 아티팩트를 검증하고 상세 검증 결과를 정책 엔진용 JSON 형식으로 출력:

`gh {{[at|attestation]}} verify {{경로/대상/아티팩트.bin}} {{[-o|--owner]}} {{조직_이름}} --format json`

- 다운로드한 번들, 사용자 지정 신뢰 루트 파일을 사용해 완전한 오프라인 검증 수행:

`gh {{[at|attestation]}} verify {{경로/대상/아티팩트.bin}} {{[-b|--bundle]}} {{경로/대상/번들.jsonl}} --custom-trusted-root {{경로/대상/신뢰가능한_루트.jsonl}}`

- 오프라인 검증용 서명 인증서의 신뢰 루트를 파일로 저장:

`gh {{[at|attestation]}} trusted-root > {{경로/대상/신뢰가능한_루트.jsonl}}`
