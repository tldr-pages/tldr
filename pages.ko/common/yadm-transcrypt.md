# yadm transcrypt

> `transcrypt`가 설치된 경우, 이 명령을 통해 `transcrypt`에 직접 옵션을 전달할 수 있습니다.
> yadm 저장소를 사용하도록 환경이 구성되어 있습니다.
> Transcrypt는 Git 저장소의 파일에 대해 투명한 암호화 및 복호화를 지원합니다.
> 더 많은 정보: <https://github.com/elasticdog/transcrypt>.

- 암호화에 사용할 대칭 암호 설정:

`yadm transcrypt --cipher={{암호}}`

- 키를 유도할 암호 전달:

`yadm transcrypt --password={{암호}}`

- 예를 가정하고 지정되지 않은 옵션에 대해 기본값 수락:

`yadm transcrypt --yes`

- 현재 저장소의 암호와 암호 표시:

`yadm transcrypt --display`

- 새로운 자격 증명을 사용하여 모든 암호화된 파일을 다시 암호화:

`yadm transcrypt --rekey`
