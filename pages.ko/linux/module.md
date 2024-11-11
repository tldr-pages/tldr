# module

> 사용자의 환경을 module 명령어로 수정.
> 더 많은 정보: <https://lmod.readthedocs.io/en/latest/010_user.html>.

- 사용 가능한 모듈 표시:

`module avail`

- 이름으로 모듈 검색:

`module avail {{모듈_이름}}`

- 모듈 로드:

`module load {{모듈_이름}}`

- 로드된 모듈 표시:

`module list`

- 특정 로드된 모듈 언로드:

`module unload {{모듈_이름}}`

- 모든 로드된 모듈 언로드:

`module purge`

- 사용자가 생성한 모듈 지정:

`module use {{경로/대상/모듈_파일1 경로/대상/모듈_파일2 ...}}`
