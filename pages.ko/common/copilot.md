# copilot

> GitHub Copilot과 상호작용하는 CLI 도궄.
> 더 많은 정보: <https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli>.

- 인터렉티브 모드 시작:

`copilot`

- 모든 파일 편집 허용:

`copilot --allow-tool write`

- 가장 최근 세션 이어서 실행:

`copilot --continue`

- 세션 선택기를 통해 이전 세션 이어서 실행:

`copilot --resume`

- 특정 모델 사용:

`copilot --model "{{gpt-5}}"`

- `git push`를 제외한 모든 Git 명령 허용:

`copilot --allow-tool 'shell(git:*)' --deny-tool 'shell(git push)'`

- 인터렉티브 모드 없이 프롬프트 직접 실행 (모든 명령을 `copilot`가 사용 가능하게 허용):

`copilot {{[-p|--prompt]}} "{{Fix the bug in main.js}}" --allow-all-tools`
