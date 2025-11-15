# dust

> Dust는 어떤 디렉토리가 디스크 공간을 사용하고 있는지에 대한 즉각적인 개요를 제공.
> 더 많은 정보: <https://github.com/bootandy/dust#usage>.

- 현재 디렉토리에 대한 정보 표시:

`dust`

- 하나 이상의 디렉토리에 대한 정보를 표시:

`dust {{경로/대상/디렉터리1 경로/대상/디렉터리2 ...}}`

- 30개 디렉터리 표시 (기본값은 21):

`dust --number-of-lines {{30}}`

- 현재 디렉토리에 대한 정보를, 최대 3단계까지 표시:

`dust --depth {{3}}`

- 가장 큰 디렉토리를 내림차순으로 맨 위에 표시:

`dust --reverse`

- 특정 이름을 가진 모든 파일과 디렉터리를 무시:

`dust --ignore-directory {{파일_또는_디렉터리_이름}}`

- 백분율 막대 및 백분율을 표시하지 않음:

`dust --no-percent-bars`
