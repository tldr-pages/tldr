# gyb

> HTTPS를 통해 Gmail API를 사용하여 Gmail 메시지를 로컬로 백업.
> 더 많은 정보: <https://github.com/GAM-team/got-your-back>.

- Gmail 계정에 있는 모든 이메일의 수와 크기를 추정:

`gyb --email {{email@gmail.com}} --action estimate`

- Gmail 계정을 특정 디렉토리에 백업:

`gyb --email {{email@gmail.com}} --action backup --local-folder {{경로/대상/디렉토리}}`

- Gmail 계정에서 중요하거나 별표 표시된 이메일만 기본 로컬 폴더에 백업:

`gyb --email {{email@gmail.com}} --search "{{is:important OR is:starred}}"`

- 로컬 폴더에서 Gmail 계정에서 복원:

`gyb --email {{email@gmail.com}} --action restore --local-folder {{경로/대상/디렉토리}}`
