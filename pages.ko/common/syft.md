# syft

> 컨테이너 이미지와 파일 시스템에서 SBOM(Software Bill of Materials)을 생성.
> 더 많은 정보: <https://oss.anchore.com/docs/reference/syft/cli/>.

- 컨테이너 이미지에서 SBOM 생성:

`syft {{image:tag}}`

- 로컬 디렉터리에서 SBOM 생성:

`syft {{경로/대상/디렉터리}}`

- 컨테이너 아카이브 파일에서 SBOM 생성:

`syft {{경로/대상/아카이브.tar}}`

- SPDX JSON 형식으로 SBOM 생성:

`syft {{이미지:태그}} {{[-o|--output]}} spdx-json`

- CycloneDX JSON 형식으로 SBOM 생성:

`syft {{이미지:태그}} {{[-o|--output]}} cyclonedx-json`

- 지정한 형식으로 SBOM을 파일에 저장:

`syft {{이미지:태그}} {{[-o|--output]}} {{형식}}={{경로/대상/출력_파일}}`

- 도움말 표시:

`syft {{[-h|--help]}}`

- 버전 정보 표시:

`syft --version`
