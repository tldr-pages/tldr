# fallocate

> 파일에 디스크 공간을 예약하거나 할당 해제.
> 이 도구는 공간을 할당할 때 0으로 초기화하지 않습니다.
> 더 많은 정보: <https://manned.org/fallocate>.

- 700 MiB의 디스크 공간을 차지하는 파일 예약:

`fallocate {{[-l|--length]}} 700M {{경로/대상/파일}}`

- 이미 할당된 파일을 200 MB 줄이기:

`fallocate {{[-c|--collapse-range]}} {{[-l|--length]}} 200MB {{경로/대상/파일}}`

- 파일에서 100 MiB 이후의 20 MB 공간 줄이기:

`fallocate {{[-c|--collapse-range]}} {{[-o|--offset]}} 100M {{[-l|--length]}} 20M {{경로/대상/파일}}`
