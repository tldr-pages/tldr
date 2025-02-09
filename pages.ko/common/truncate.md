# truncate

> 파일의 크기를 지정된 크기로 줄이거나 늘립니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html>.

- 기존 파일의 크기를 10GB로 설정하거나, 지정된 크기로 새 파일 생성:

`truncate --size 10G {{경로/대상/파일}}`

- 파일 크기를 50MiB 늘리고, 구멍으로 채우기 (0바이트로 읽힘):

`truncate --size +50M {{경로/대상/파일}}`

- 파일의 끝에서 데이터를 제거하여 2GiB 줄이기:

`truncate --size -2G {{경로/대상/파일}}`

- 파일 내용 비우기:

`truncate --size 0 {{경로/대상/파일}}`

- 파일 내용 비우기, 파일이 존재하지 않으면 생성하지 않기:

`truncate --no-create --size 0 {{경로/대상/파일}}`
