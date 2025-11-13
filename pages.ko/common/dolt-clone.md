# dolt clone

> 저장소를 새로운 디렉터리에 복제.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-clone>.

- 기존 저장소를 특정 디렉터리에 복제 (기본값은 저장소 이름):

`dolt clone {{레포지토리_주소}} {{경로/대상/디렉터리}}`

- 기존 저장소를 복제하고 특정 원격값을 추가 (기본값은 origin):

`dolt clone --remote {{원격_이름}} {{레포지토리_주소}}`

- 특정 브랜치만 가져오는 기존 저장소를 복제 (기본값은 모든 브랜치):

`dolt clone --branch {{브랜치_이름}} {{레포지토리_주소}}`

- AWS 리전을 사용하여, 리포지토리를 복제 (uses the profile's default region if none is provided):

`dolt clone --aws-region {{리전_이름}} {{레포지토리_주소}}`

- AWS 자격 증명 파일을 사용하여 리포지토리를 복제:

`dolt clone --aws-creds-file {{인증_파일}} {{레포지토리_주소}}`

- AWS 자격 증명 프로필을 사용하여 리포지토리를 복제 (아무것도 제공되지 않은 경우, 기본 프로필을 사용):

`dolt clone --aws-creds-profile {{프로필_이름}} {{레포지토리_주소}}`

- AWS 자격 증명 유형을 사용하여 리포지토리를 복젴:

`dolt clone --aws-creds-type {{인증_타입}} {{레포지토리_주소}}`
