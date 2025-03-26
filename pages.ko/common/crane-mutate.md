# crane mutate

> 이미지 라벨과 주석을 수정.
> 컨테이너를 레지스트리에 푸시해야 하며, 매니페스트가 레지스트리에서 업데이트.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>.

- 새로운 주석을 설정 (기본값 []):

`crane mutate {{[-a|--annotation]}}/{{[-l|--label]}} {{annotation/label}}`

- 이미지에 추가할 tarball/command/entrypoint/environment variable/exposed-ports의 경로를 지정:

`crane mutate {{--append}}/{{--cmd}}/{{--entrypoint}}/{{[-e|--env]}}/{{--exposed-ports}} {{var1 var2 ...}}`

- 결과 이미지의 새로운 tarball 경로:

`crane mutate {{[-o|--output]}} {{경로/대상/tarball}}`

- 변형된 이미지를 푸시하기 위한 os/arch{{/variant}}{{:osversion}}{{,<platform>}} 형식의 저장소:

`crane mutate --set-platform {{플랫폼_이름}}`

- 변형된 이미지에 적용할 새로운 태그를 참조:

`crane mutate {{[-t|--tag]}} {{태그_이름}}`

- 새로운 사용자 설정:

`crane mutate {{[-u|--user]}} {{사용자명}}`

- 설정할 새로운 작업 디렉토리 설정:

`crane mutate {{[-w|--workdir]}} {{경로/대상/작업디렉토리}}`

- 도움말 표시:

`crane mutate {{[-h|--help]}}`
