# vault

> HashiCorp Vault와 상호작용.
> 더 많은 정보: <https://www.vaultproject.io/docs/commands>.

- Vault 서버에 연결하고 새로운 암호화 데이터 저장소 초기화:

`vault init`

- 암호화된 데이터 저장소에 접근하기 위해 필요한 키 공유 중 하나를 제공하여 금고의 잠금 해제:

`vault unseal {{키_공유_x}}`

- 인증 토큰을 사용하여 Vault 서버에 대해 CLI 클라이언트 인증:

`vault auth {{인증_토큰}}`

- "secret"이라는 일반 백엔드를 사용하여 금고에 새 비밀 저장:

`vault write secret/{{hello}} value={{world}}`

- "secret"이라는 일반 백엔드를 사용하여 금고에서 값 읽기:

`vault read secret/{{hello}}`

- 값에서 특정 필드 읽기:

`vault read -field={{필드_이름}} secret/{{hello}}`

- 데이터 저장소의 암호화 키를 메모리에서 제거하여 Vault 서버 잠금:

`vault seal`
