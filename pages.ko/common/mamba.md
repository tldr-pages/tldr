# mamba

> 빠르고 플랫폼 간에 호환되는 패키지 관리자로, conda의 대체품으로 설계되었습니다.
> `repoquery`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- 새 환경을 생성하고 지정한 패키지를 설치:

`mamba create --name {{환경_이름}} {{python=3.10 matplotlib}}`

- 현재 환경에 패키지를 설치하고 패키지 [c]hannel을 지정:

`mamba install -c {{conda-forge}} {{python=3.6 numpy}}`

- 현재 환경의 모든 패키지 업데이트:

`mamba update --all`

- 저장소에서 특정 패키지 검색:

`mamba repoquery search {{numpy}}`

- 모든 환경 나열:

`mamba info --envs`

- 캐시에서 사용되지 않는 [p]패키지 및 [t]타르볼 제거:

`mamba clean -pt`

- 환경 활성화:

`mamba activate {{환경_이름}}`

- 현재 활성화된 환경에 설치된 모든 패키지 나열:

`mamba list`
