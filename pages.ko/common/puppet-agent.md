# puppet agent

> Puppet 서버에서 클라이언트 구성을 가져와 로컬 호스트에 적용.
> 더 많은 정보: <https://github.com/puppetlabs/puppet/blob/main/references/man/agent.md>.

- Puppet 서버에 노드를 등록하고 받은 카탈로그 적용:

`puppet agent --test --server {{puppetserver_fqdn}} --serverport {{포트}} --waitforcert {{poll_time}}`

- 에이전트를 백그라운드에서 실행 (`puppet.conf`의 설정 사용):

`puppet agent`

- 포그라운드에서 한 번 에이전트를 실행한 후 종료:

`puppet agent --test`

- 드라이 모드로 에이전트 실행:

`puppet agent --test --noop`

- 평가 중인 모든 리소스를 로그에 기록 (변경 사항이 없어도):

`puppet agent --test --evaltrace`

- 에이전트 비활성화:

`puppet agent --disable "{{메시지}}"`

- 에이전트 활성화:

`puppet agent --enable`
