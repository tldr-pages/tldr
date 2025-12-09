# kubectl label

> Kubernetes 리소스에 레이블 지정.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_label>.

- 포드에 레이블 지정:

`kubectl label pod {{포드_이름}} {{키}}={{값}}`

- 기존 값을 덮어쓰며 포드 레이블 업데이트:

`kubectl label --overwrite pod {{포드_이름}} {{키}}={{값}}`

- 네임스페이스의 모든 포드에 레이블 지정:

`kubectl label pods --all {{키}}={{값}}`

- 포드 정의 파일로 식별된 포드에 레이블 지정:

`kubectl label {{[-f|--filename]}} {{포드_정의_파일}} {{키}}={{값}}`

- 포드에서 레이블 제거:

`kubectl label pod {{포드_이름}} {{키}}-`
