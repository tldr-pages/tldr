# rekor-cli

> 소프트웨어 프로젝트의 공급망 내에서 생성된 메타데이터의 변경 불가능한 변조 방지 원장.
> 더 많은 정보: <https://github.com/sigstore/rekor>.

- 아티팩트를 Rekor에 업로드:

`rekor-cli upload --artifact {{경로/대상/파일.ext}} --signature {{경로/대상/파일.ext.sig}} --pki-format={{x509}} --public-key={{경로/대상/키.pub}}`

- 투명성 로그의 항목에 대한 정보 얻기:

`rekor-cli get --uuid={{0e81b4d9299e2609e45b5c453a4c0e7820ac74e02c4935a8b830d104632fd2d1}}`

- 아티팩트로 Rekor 색인에서 항목 검색:

`rekor-cli search --artifact {{경로/대상/파일.ext}}`

- 특정 해시로 Rekor 색인에서 항목 검색:

`rekor-cli search --sha {{6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b}}`
