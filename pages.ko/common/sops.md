# sops

> SOPS (Secrets OPerationS): 비밀 관리를 위한 간단하고 유연한 도구.
> 더 많은 정보: <https://github.com/getsops/sops>.

- 파일 암호화:

`sops -e {{경로/대상/파일.json}} > {{경로/대상/파일.enc.json}}`

- 파일을 `stdout`으로 복호화:

`sops -d {{경로/대상/파일.enc.json}}`

- `sops` 파일에서 선언된 키 업데이트:

`sops updatekeys {{경로/대상/파일.enc.yaml}}`

- `sops` 파일의 데이터 키 회전:

`sops -r {{경로/대상/파일.enc.yaml}}`

- 파일 암호화 후 확장자 변경:

`sops -d --input-type json {{경로/대상/파일.enc.json}}`

- 이름으로 키를 추출하고, 번호로 배열 요소 추출:

`sops -d --extract '["an_array"][1]' {{경로/대상/파일.enc.json}}`

- 두 `sops` 파일 간의 차이점 표시:

`diff <(sops -d {{경로/대상/secret1.enc.yaml}}) <(sops -d {{경로/대상/secret2.enc.yaml}})`
