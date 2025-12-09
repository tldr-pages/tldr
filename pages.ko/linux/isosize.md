# isosize

> ISO 파일의 크기를 표시합니다.
> 더 많은 정보: <https://manned.org/isosize>.

- ISO 파일의 크기 표시:

`isosize {{경로/대상/파일.iso}}`

- ISO 파일의 블록 수와 블록 크기 표시:

`isosize --sectors {{경로/대상/파일.iso}}`

- 주어진 수로 나눈 ISO 파일의 크기 표시 (--sectors 옵션이 없는 경우에만 사용 가능):

`isosize --divisor={{숫자}} {{경로/대상/파일.iso}}`
