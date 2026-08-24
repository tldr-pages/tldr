# oneliner

> 영어를 OpenAI, Claude, 로컬 LLM을 사용해 쉘 명령으로 변환하는 도구(사용자 지식 대체가 아닌, 학습을 돕는 것을 목표로 함).
> 더 많은 정보: <https://github.com/dorochadev/oneliner#-usage-flags>.

- 영어로부터 쉘 명령 생성:

`oneliner "{{find all jpg files larger than 10MB}}"`

- 명령이 수행하는 작업 설명:

`oneliner {{[-e|--explain]}} "{{delete node_modules recursively}}"`

- 생성된 명령을 클립보드에 복사:

`oneliner {{[-c|--clipboard]}} "{{compress all pdfs}}"`

- 명령을 교육적인 관점에서, 자세히 분석하여 설명:

`oneliner {{[-b|--breakdown]}} "{{list all active network connections}}"`

- 생성된 명령 실행 (사용에 주의가 필요):

`oneliner {{[-r|--run]}} "{{list files larger than 1GB}}"`

- 생성된 명령 실행 전에 대화형으로 확인 요청:

`oneliner {{[-i|--interactive]}} "{{delete temporary files in /tmp}}"`
