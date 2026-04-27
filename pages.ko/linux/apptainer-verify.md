# apptainer verify

> SIF 컨테이너 이미지의 디지털 서명을 검증하는 도구.
> 관련 항목: `apptainer-sign`.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_verify.html>.

- 기본 PGP 키링을 사용하여 컨테이너 이미지 검증:

`apptainer verify {{경로/대상/이미지.sif}}`

- 특정 공개 키 파일을 사용하여 컨테이너 이미지 검증:

`apptainer verify --key {{경로/대상/공개키.pem}} {{경로/대상/이미지.sif}}`

- 인증서 파일을 사용하여 컨테이너 이미지 검증:

`apptainer verify --certificate {{경로/대상/인증서.pem}} {{경로/대상/이미지.sif}}`

- 이미지의 모든 객체 검증:

`apptainer verify {{[-a|--all]}} {{경로/대상/이미지.sif}}`

- 이미지 내 특정 객체 그룹 검증:

`apptainer verify {{[-g|--group-id]}} {{그룹_아이디}} {{경로/대상/이미지.sif}}`

- 이미지 내 특정 객체 ID 검증:

`apptainer verify {{[-i|--sif-id]}} {{객체_아이디}} {{경로/대상/이미지.sif}}`

- 검증 결과를 JSON 형식으로 출력:

`apptainer verify {{[-j|--json]}} {{경로/대상/이미지.sif}}`

- 도움말 표시:

`apptainer verify {{[-h|--help]}}`
