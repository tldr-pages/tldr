# oc

> OpenShift 컨테이너 플랫폼 CLI.
> 애플리케이션 및 컨테이너 관리를 허용합니다.
> 더 많은 정보: <https://docs.openshift.com/container-platform/latest/cli_reference/get_started_cli.html>.

- OpenShift 컨테이너 플랫폼 서버에 로그인:

`oc login`

- 새 프로젝트 생성:

`oc new-project {{프로젝트_이름}}`

- 기존 프로젝트로 전환:

`oc project {{프로젝트_이름}}`

- 프로젝트에 새 애플리케이션 추가:

`oc new-app {{저장소_URL}} --name {{애플리케이션}}`

- 컨테이너에 원격 셸 세션 열기:

`oc rsh {{포드_이름}}`

- 프로젝트 내 포드 나열:

`oc get pods`

- 현재 세션에서 로그아웃:

`oc logout`
