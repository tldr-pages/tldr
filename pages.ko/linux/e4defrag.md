# e4defrag

> ext4 파일 시스템을 조각 모음합니다.
> 더 많은 정보: <https://manned.org/e4defrag>.

- 파일 시스템 조각 모음:

`e4defrag {{/dev/sdXN}}`

- 파일 시스템이 얼마나 조각화되었는지 확인:

`e4defrag -c {{/dev/sdXN}}`

- 오류와 각 파일의 조각화 개수를 조각 모음 전후에 출력:

`e4defrag -v {{/dev/sdXN}}`
