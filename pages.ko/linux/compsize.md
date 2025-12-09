# compsize

> btrfs 파일 시스템에서 파일 집합의 압축 비율을 계산합니다.
> 파일을 다시 압축하기 위해 단편화를 해제하는 방법은 `btrfs filesystem`을 참조하세요.
> 더 많은 정보: <https://manned.org/compsize>.

- 파일 또는 디렉터리에 대한 현재 압축 비율 계산:

`sudo compsize {{경로/대상/파일_또는_폴더}}`

- 파일 시스템 경계를 넘지 않도록 설정:

`sudo compsize {{[-x|--one-file-system]}} {{경로/대상/파일_또는_폴더}}`

- 사람이 읽을 수 있는 크기 대신 원시 바이트 수를 표시:

`sudo compsize {{[-b|--bytes]}} {{경로/대상/파일_또는_폴더}}`
