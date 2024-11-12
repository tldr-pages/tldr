# corepack

> Node 프로젝트와 해당 패키지 관리자 사이의 브라지 역할을 하는 런타임 종속성이 없는 패키지.
> 더 많은 정보: <https://github.com/nodejs/corepack>.

- Corepack shim을 Node.js 설치 디렉터리에 추가하여 전역 명령으로 사용할 수 있도록 함:

`corepack enable`

- 특정 디렉토리에 Corepack shim을 추가함:

`corepack enable --install-directory {{경로/대상/디렉토리}}`

- Node.js 설치 디렉터리에서 Corepack shim을 제거:

`corepack disable`

- 특정 패키지 관리자를 준비:

`corepack prepare {{패키지_매니저}}@{{버전}} --activate`

- 현재 경로의 프로젝트에 대해 구성된 패키지 관리자를 준비:

`corepack prepare`

- 전역 명령으로 설치하지 않고 패키지 관리자를 사용:

`corepack {{npm|pnpm|yarn}} {{패키지_매니저_인자}}`

- 지정된 아카이브에서 패키지 관리자를 설치:

`corepack hydrate {{경로/대상/corepack.tgz}}`

- 하위 명령어에 대한 도움말 표시:

`corepack {{하위명령어}} --help`
