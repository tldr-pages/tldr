# trivy

> 컨테이너 이미지, 파일 시스템 및 Git 저장소의 취약점과 구성 문제를 스캔하는 도구.
> 더 많은 정보: <https://aquasecurity.github.io/trivy>.

- Docker 이미지를 취약점 및 노출된 비밀 키에 대해 스캔:

`trivy image {{이미지:태그}}`

- 심각도에 따라 출력 결과를 필터링하여 Docker 이미지 스캔:

`trivy image --severity {{HIGH,CRITICAL}} {{alpine:3.15}}`

- 수정되지 않거나 패치되지 않은 취약점을 무시하고 Docker 이미지 스캔:

`trivy image --ignore-unfixed {{alpine:3.15}}`

- 파일 시스템을 취약점 및 잘못된 구성에 대해 스캔:

`trivy fs --security-checks {{vuln,config}} {{경로/대상/프로젝트_폴더}}`

- IaC(Terraform, CloudFormation, ARM, Helm 및 Dockerfile) 디렉토리를 잘못된 구성에 대해 스캔:

`trivy config {{경로/대상/iac_폴더}}`

- 로컬 또는 원격 Git 저장소를 취약점에 대해 스캔:

`trivy repo {{경로/대상/로컬_저장소_폴더|원격_저장소_URL}}`

- 특정 커밋 해시까지 Git 저장소 스캔:

`trivy repo --commit {{커밋_해시}} {{저장소}}`

- SARIF 템플릿으로 출력 생성:

`trivy image --format {{template}} --template "{{@sarif.tpl}}" -o {{경로/대상/보고서.sarif}} {{이미지:태그}}`
