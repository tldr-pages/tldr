# certbot

> TLS 인증서를 자동으로 획득하고 갱신하기 위한 Let's Encrypt 에이전트.
> `letsencrypt`의 후속 도구.
> 더 많은 정보: <https://eff-certbot.readthedocs.io/en/latest/using.html>.

- 웹루트 인증을 통해 새 인증서를 획득하지만 자동으로 설치하지 않기:

`sudo certbot certonly --webroot {{[-w|--webroot-path]}} {{경로/대상/웹루트}} {{[-d|--domain]}} {{서브도메인.example.com}}`

- nginx 인증을 통해 새 인증서를 획득하고 자동으로 설치하기:

`sudo certbot --nginx {{[-d|--domain]}} {{서브도메인.example.com}}`

- apache 인증을 통해 새 인증서를 획득하고 자동으로 설치하기:

`sudo certbot --apache {{[-d|--domain]}} {{서브도메인.example.com}}`

- 30일 이내에 만료되는 모든 Let's Encrypt 인증서 갱신하기 (사용하고 있는 서버를 잊지 말고 재시작하기):

`sudo certbot renew`

- 새 인증서 획득을 시뮬레이션하지만 실제로 디스크에 인증서를 저장하지 않기:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{경로/대상/웹루트}} {{[-d|--domain]}} {{서브도메인.example.com}} --dry-run`

- 신뢰할 수 없는 테스트 인증서 획득하기:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{경로/대상/웹루트}} {{[-d|--domain]}} {{서브도메인.example.com}} --test-cert`
