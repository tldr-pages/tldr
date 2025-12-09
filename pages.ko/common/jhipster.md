# jhipster

> 모놀리식 또는 마이크로서비스 아키텍처를 사용하는 웹 애플리케이션 생성기.
> 더 많은 정보: <https://www.jhipster.tech/creating-an-app/#command-line-options>.

- 간단한 풀스택 프로젝트 생성 (모놀리식 또는 마이크로서비스):

`jhipster`

- 간단한 프론트엔드 프로젝트 생성:

`jhipster --skip-server`

- 간단한 백엔드 프로젝트 생성:

`jhipster --skip-client`

- 프로젝트에 최신 JHipster 업데이트 적용:

`jhipster upgrade`

- 생성된 프로젝트에 새로운 엔티티 추가:

`jhipster entity {{엔티티_이름}}`

- JDL 파일을 가져와 애플리케이션 구성 (참고: <https://start.jhipster.tech/jdl-studio/>):

`jhipster import-jdl {{첫번째_파일.jh 두번째_파일.jh ... n번째_파일.jh}}`

- 애플리케이션을 위한 CI/CD 파이프라인 생성:

`jhipster ci-cd`

- 애플리케이션을 위한 Kubernetes 구성 생성:

`jhipster kubernetes`
