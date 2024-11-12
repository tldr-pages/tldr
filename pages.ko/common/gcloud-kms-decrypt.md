# gcloud kms decrypt

> Cloud KMS 키를 사용하여 암호화된 파일 복호화.
> 같이 보기: `gcloud`.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/kms/decrypt>.

- 지정된 키, 키 링 및 위치를 사용하여 파일 복호화:

`gcloud kms decrypt --key={{키_이름}} --keyring={{키_링_이름}} --location={{global}} --ciphertext-file={{경로/대상/암호문}} --plaintext-file={{경로/대상/평문}}`

- 추가 인증 데이터를 사용하여 파일을 복호화하고 복호화된 평문을 `stdout`에 출력:

`gcloud kms decrypt --key={{키_이름}} --keyring={{키_링_이름}} --location={{global}} --additional-authenticated-data-file={{경로/대상/파일.aad}} --ciphertext-file={{경로/대상/암호문}} --plaintext-file=-`
