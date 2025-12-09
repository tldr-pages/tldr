# modinfo

> 리눅스 커널 모듈에 대한 정보를 추출합니다.
> 더 많은 정보: <https://manned.org/modinfo>.

- 커널 모듈의 모든 속성을 나열:

`modinfo {{커널_모듈}}`

- 지정된 속성만 나열:

`modinfo -F {{author|description|license|parm|filename}} {{커널_모듈}}`
