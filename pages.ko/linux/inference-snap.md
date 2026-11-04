# Inference snap

> 인터넷 연결 없이 로컬에서 실행되는 생성형 AI 언어 모델과 대화.
> inference-snap은 `deepseek-r1`, `gemma3`, `gemma4`, `nemotron3-nano`, `qwen-vl` 등의 모델을 지원.
> 더 많은 정보: <https://documentation.ubuntu.com/inference-snaps/>.

- 터미널에서 채팅 시작 (최초 실행 시 백그라운드에서 채팅 서버도 함께 시작):

`{{inference-snap}} chat`

- 현재 엔진과 채팅 서버 상태 표시:

`{{inference-snap}} status`

- 사용할 엔진 선택 (예: NVIDIA GPU용 `cuda`). 해당 엔진에 맞는 모델 다운로드 및 사용:

`sudo {{inference-snap}} use-engine {{엔진}}`

- 장치의 상세 하드웨어 정보(RAM, architecture 등) 표시:

`sudo {{inference-snap}} show-machine`

- 실행 중인 채팅 서버의 모든 설정 (`http.host`, `http.port`) 표시:

`{{inference-snap}} get`
