# msbuild

> Visual Studio 프로젝트 솔루션을 위한 Microsoft 빌드 도구.
> 더 많은 정보: <https://learn.microsoft.com/visualstudio/msbuild>.

- 현재 디렉토리의 첫 번째 프로젝트 파일 빌드:

`msbuild`

- 특정 프로젝트 파일 빌드:

`msbuild {{경로/대상/프로젝트_파일}}`

- 빌드할 하나 이상의 세미콜론으로 구분된 타겟 지정:

`msbuild {{경로/대상/프로젝트_파일}} /target:{{타겟들}}`

- 하나 이상의 세미콜론으로 구분된 속성 지정:

`msbuild {{경로/대상/프로젝트_파일}} /property:{{이름=값}}`

- 사용할 빌드 도구 버전 지정:

`msbuild {{경로/대상/프로젝트_파일}} /toolsversion:{{버전}}`

- 프로젝트가 어떻게 구성되었는지에 대한 자세한 정보를 로그 끝에 표시:

`msbuild {{경로/대상/프로젝트_파일}} /detailedsummary`

- 도움말 표시:

`msbuild /help`
