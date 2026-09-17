# bwrap

> 경량 샌드박스 환경에서 프로그램을 실행하는 도구.
> 더 많은 정보: <https://manned.org/bwrap>.

- 읽기 전용 환경에서의 프로그램 실행:

`bwrap --ro-bind / / {{/bin/bash}}`

- 장치/프로세스 정보 접근 허용하고 `tmpfs` 생성 후 실행:

`bwrap --dev-bind /dev /dev --proc /proc --ro-bind / / --tmpfs /tmp {{/bin/bash}}`
