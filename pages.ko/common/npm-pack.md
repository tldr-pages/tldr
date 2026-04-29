# npm pack

> 패키지로부터 tarball 파일을 생성하는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/pack/>.

- 현재 디렉터리의 패키지로 tarball 생성:

`npm pack`

- Create a tarball from a specific package folder:

`npm pack {{path/to/package_directory}}`

- Run a dry run to preview the tarball contents without creating it:

`npm pack --dry-run`

- Create a tarball without running lifecycle scripts:

`npm pack --ignore-scripts`

- Specify a custom registry to fetch package metadata from:

`npm pack --registry {{https://registry.npmjs.org/}}`
