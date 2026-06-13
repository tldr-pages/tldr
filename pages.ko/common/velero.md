# velero

> Kubernetes 애플리케이션 및 그들의 지속 볼륨을 백업 및 마이그레이션.
> 더 많은 정보: <https://velero.io/docs/main/>.

- 모든 리소스를 포함하는 백업 생성:

`velero backup create {{백업_이름}}`

- 모든 백업 나열:

`velero backup get`

- 백업 삭제:

`velero backup delete {{백업_이름}}`

- 주간 백업 생성, 각각 90일(2160시간) 동안 유지:

`velero schedule create {{스케줄_이름}} --schedules="{{@every 7d}}" --ttl {{2160h0m0s}}`

- 특정 스케줄에 의해 트리거된 최신 성공적인 백업에서 복원 생성:

`velero restore create --from-schedule {{스케줄_이름}}`
