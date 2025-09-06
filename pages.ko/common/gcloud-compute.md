# gcloud compute

> Google Cloud 인프라에서 VM을 생성, 실행 및 관리.
> 같이 보기: `gcloud`.
> 더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/compute>.

- Compute Engine 영역 나열:

`gcloud compute zones list`

- VM 인스턴스 생성:

`gcloud compute instances create {{인스턴스_이름}}`

- VM 인스턴스 세부 정보 표시:

`gcloud compute instances describe {{인스턴스_이름}}`

- 프로젝트 내 모든 VM 인스턴스 나열:

`gcloud compute instances list`

- 영구 디스크 스냅샷 생성:

`gcloud compute disks snapshot {{디스크_이름}} --snapshot-names {{스냅샷_이름}}`

- 스냅샷 세부 정보 표시:

`gcloud compute snapshots describe {{스냅샷_이름}}`

- 스냅샷 삭제:

`gcloud compute snapshots delete {{스냅샷_이름}}`

- SSH를 사용하여 VM 인스턴스에 연결:

`gcloud compute ssh {{인스턴스_이름}}`
