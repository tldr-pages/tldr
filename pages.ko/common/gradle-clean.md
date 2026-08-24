# gradle clean

> 빌드 디렉터리와 생성된 모든 파일 삭제.
> 더 많은 정보: <https://docs.gradle.org/current/userguide/command_line_interface.html#cleaning_outputs>.

- 빌드 디렉터리 정리:

`gradle clean`

- 정리 후 프로젝트 빌드 수행:

`gradle clean build`

- 멀티 프로젝트 빌드에서 특정 하위 프로젝트 정리:

`gradle :{{하위_프로젝트}}:clean`

- 더 자세한 로그와 함께 정리 수행:

`gradle clean {{[-i|--info]}}`
