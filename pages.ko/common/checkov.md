# checkov

> Checkov는 IaC(Infrastructure as Code)를 위한 정적 코드 분석 도구.
> 이미지 및 오픈소스 패키지를 위한 SCA(소프트웨어 구성 분석) 도구.
> 더 많은 정보: <https://www.checkov.io/1.Welcome/Quick%20Start.html>.

- IaC(Terraform, Cloudformation, ARM, Ansible, Bicep, Dockerfile 등)가 포함된 디렉터리를 스캔:

`checkov --directory {{경로/대상/디렉터리}}`

- 출력에서 코드 블록을 생략하고 IaC 파일을 스캔:

`checkov --compact --file {{경로/대상/파일}}`

- 모든 IaC 유형에 대한 모든 검사를 나열:

`checkov --list`
