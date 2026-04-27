# mvn deploy

> 아티팩트를 원격 저장소에 배포하는 명령어.
> 더 많은 정보: <https://manned.org/mvn>.

- `settings.xml` 파일에 설정된 원격 저장소로 최종 아티팩트 업로드:

`mvn deploy`

- Copy an artifact, that is not built using Maven to the remote repository:

`mvn deploy:deploy-file {{[-D|--define]}} url={{원격_저장소_url}} {{[-D|--define]}} repositoryId={{settings.xml에_설정된_서버_아이디}} {{[-D|--define]}} file={{배포될_파일}}`
