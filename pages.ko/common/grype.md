# grype

> 컨테이너 이미지 및 파일 시스템의 취약점 스캐너.
> 더 많은 정보: <https://oss.anchore.com/docs/reference/grype/cli>.

- 컨테이너 이미지 스캔:

`grype {{이미지:태그}}`

- 특정 형식으로 결과 출력하며 이미지 스캔:

`grype {{이미지:태그}} {{[-o|--output]}} {{json|table|cyclonedx|cyclonedx-json|sarif|template}}`

- 수정되지 않은 취약점은 제외하고 이미지 스캔:

`grype {{이미지:태그}} --only-fixed`

- 지정한 심각도 이상 취약점 발견 시, 실패로 표시하고 이미지 스캔:

`grype {{이미지:태그}} {{[-f|--fail-on]}} {{negligible|low|medium|high|critical}}`

- 로컬 디렉터리를 스캔하고 보고서를 파일로 저장:

`grype {{경로/대상/디렉터리}} --file {{경로/대상/리포트}}`

- 취약점 데이터베이스 업데이트:

`grype db update`

- 현재 데이터베이스 상태 표시:

`grype db status`

- 도움말 표시:

`grype {{[-h|--help]}}`
