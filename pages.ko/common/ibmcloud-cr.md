# ibmcloud cr

> IBM Cloud Container Registry 콘텐츠 및 설정 관리.
> 더 많은 정보: <https://cloud.ibm.com/docs/cli?topic=cli-containerregcli>.

- IBM Cloud Container Registry 대상 리전 설정:

`ibmcloud cr region-set`

- 사용 가능한 이미지 목록 표시:

`ibmcloud cr {{[images|image-list]}}`

- 이미지 정보 검사:

`ibmcloud cr image-inspect {{이미지}}`

- 이미지 취약점 평가 수행:

`ibmcloud cr {{[va|vulnerability-assessment]}} {{이미지}}`

- 로컬 Docker 또는 Podman 클라이언트를 IBM Cloud Container Registry에 로그인:

`ibmcloud cr login`

- 이 명령에서 사용 가능한 모든 작업 목록 표시:

`ibmcloud cr help`
