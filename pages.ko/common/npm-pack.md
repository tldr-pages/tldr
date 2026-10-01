# npm pack

> 패키지로부터 tarball 파일을 생성하는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/pack/>.

- 현재 디렉터리의 패키지로 tarball 생성:

`npm pack`

- 지정한 패키지 디렉터리에서 tarball을 생성:

`npm pack {{경로/대상/패키지_디렉터리}}`

- tarball을 생성하지 않고 포함될 내용을 미리 확인:

`npm pack --dry-run`

- lifecycle 스크립트를 실행하지 않고 tarball 생성:

`npm pack --ignore-scripts`

- 패키지 메타데이터를 가져올 사용자 지정 레지스트리 지정:

`npm pack --registry {{https://registry.npmjs.org/}}`
