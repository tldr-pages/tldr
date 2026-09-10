# doctl invoice

> DigitalOcean 계정의 청구서 상세 정보 조회.
> 더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/invoice/>.

- 모든 청구서 목록 표시:

`doctl invoice list`

- 지정한 청구서에 포함된 리소스 세부 항목 목록을 조회:

`doctl invoice get {{청구서_uuid}}`

- 지정한 청구서의 요약 정보 조회:

`doctl invoice summary {{청구서_uuid}}`

- 지정한 청구서를 PDF 파일로 다운로드:

`doctl invoice pdf {{청구서_uuid}}`

- 지정한 청구서를 CSV 파일로 다운로드:

`doctl invoice csv {{청구서_uuid}}`
