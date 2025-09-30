# mamba repoquery

> conda 및 mamba 패키지 저장소와 패키지 의존성을 효율적으로 조회.
> 더 많은 정보: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>.

- 특정 패키지의 사용 가능한 모든 버전 검색:

`mamba repoquery search {{패키지}}`

- 특정 제약 조건을 만족하는 모든 패키지 검색:

`mamba repoquery search {{sphinx<5}}`

- 현재 활성화된 환경에 설치된 패키지의 의존성을 트리 형식으로 나열:

`mamba repoquery depends --tree {{scipy}}`

- 특정 패키지의 설치가 필요한 현재 환경의 패키지를 출력 (`depends`의 역방향):

`mamba repoquery whoneeds {{ipython}}`
