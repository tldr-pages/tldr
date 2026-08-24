# kubeseal

> Bitnami Sealed Secrets 컨트롤러를 사용하여 Kubernetes secret를 암호화하는 클라이언트 측 유틸리티.
> 버전 관리에 안전하게 저장할 수 있는 SealedSecret 리소스 생성.
> 클러스터에 컨트롤러가 실행 중이어야 함 (예: `kubectl apply --filename controller.yaml`로 설치).
> 더 많은 정보: <https://github.com/bitnami-labs/sealed-secrets>.

- YAML 파일의 Kubernetes secret을 SealedSecret으로 암호화 (기본 출력: JSON):

`kubeseal < {{secret.yaml}} > {{sealedsecret.json}}`

- API 인증용 bearer token을 사용하여 secret를 암호화하고, YAML 또는 JSON 형식으로 출력:

`kubeseal < {{secret.yaml}} {{[-o|--format]}} {{yaml|json}} --token {{자신의-bearer-token}} > {{sealedsecret.yaml}}`

- sealed-secrets 컨트롤러의 특정 네임스페이스와 이름을 사용해 secret 봉인 :

`kubeseal < {{secret.yaml}} --controller-namespace {{컨트롤러-네임스페이스}} --controller-name {{컨트롤러-이름}} > {{sealedsecret.yaml}}`

- 파일의 raw secret 값을 지정한 이름과 scope로 암호화:

`kubeseal --raw --from-file {{경로/대상/secret.txt}} --name {{자신의-secret}} --scope {{strict|namespace-wide|cluster-wide}} > {{sealedsecret.yaml}}`

- basic auth로 오프리인 봉인용 컨트롤러 공개 인증서를 가져오기:

`kubeseal --fetch-cert --username {{사용자명}} --password {{비밀번호}} > {{인증서.pem}}`

- 가져온 인증서를 사용하여 오프라인으로 secret 봉인:

`kubeseal < {{secret.yaml}} --cert {{인증서.pem}} > {{sealedsecret.yaml}}`

- 기존 SealedSecret 파일에 secret을 병합하여 제자리에서 수정:

`kubeseal < {{secret.yaml}} --merge-into {{sealedsecret.yaml}}`

- SealedSecret을 적용하지 않고 검증:

`kubeseal < {{sealedsecret.yaml}} --validate`
