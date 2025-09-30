# gsutil

> Google Cloud 스토리지 접근.
> `gsutil`을 사용하여 광범위한 버킷 및 객체 관리 작업을 수행 가능.
> 더 많은 정보: <https://cloud.google.com/storage/docs/gsutil>.

- 로그인한 프로젝트의 모든 버킷을 나열:

`gsutil ls`

- 버킷의 객체를 나열:

`gsutil ls -r 'gs://{{버킷_이름}}/{{prefix}}**'`

- 버킷에서 객체 다운로드:

`gsutil cp gs://{{버킷_이름}}/{{객체_이름}} {{path/to/save_location}}`

- 버킷에 객체 업로드:

`gsutil cp {{object_location}} gs://{{목적지_버킷_이름}}/`

- 버킷의 객체 이름을 바꾸거나 객체를 이동:

`gsutil mv gs://{{버킷_이름}}/{{오래된_객체_이름}} gs://{{버킷_이름}}/{{새로운_객체_이름}}`

- 로그인한 프로젝트에서 새로운 버킷을 생성:

`gsutil mb gs://{{버킷_이름}}`

- 버킷을 삭제하고 버킷에 있는 모든 객체를 제거:

`gsutil rm -r gs://{{버킷_이름}}`
