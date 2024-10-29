# dolt clone

> 새 디렉토리에 저장소를 복제.
> 더 많은 정보: <https://docs.dolthub.com/interfaces/cli#dolt-clone>.

- 기존 저장소를 특정 디렉토리에 복제 (기본값은 저장소 이름):

`dolt clone {{저장소_URL}} {{경로/대상/폴더}}`

- 기존 저장소를 복제하고 특정 원격 추가 (기본값은 origin):

`dolt clone --remote {{원격_이름}} {{저장소_URL}}`

- 특정 브랜치만 가져와서 기존 저장소 복제 (기본값은 모든 브랜치):

`dolt clone --branch {{브랜치_이름}} {{저장소_URL}}`

- AWS 지역을 사용하여 저장소 복제 (제공하지 않으면 프로필의 기본 지역 사용):

`dolt clone --aws-region {{지역_이름}} {{저장소_URL}}`

- AWS 자격 증명 파일을 사용하여 저장소 복제:

`dolt clone --aws-creds-file {{자격증명_파일}} {{저장소_URL}}`

- AWS 자격 증명 프로필을 사용하여 저장소 복제 (제공하지 않으면 기본 프로필 사용):

`dolt clone --aws-creds-profile {{프로필_이름}} {{저장소_URL}}`

- AWS 자격 증명 유형을 사용하여 저장소 복제:

`dolt clone --aws-creds-type {{자격증명_유형}} {{저장소_URL}}`
