# tts

> 음성을 합성합니다.
> 더 많은 정보: <https://github.com/coqui-ai/TTS#command-line-tts>.

- 기본 모델로 텍스트를 음성으로 변환하고 출력을 "tts_output.wav"에 저장:

`tts --text "{{텍스트}}"`

- 제공된 모델 나열:

`tts --list_models`

- 인덱스로 모델 정보 조회:

`tts --model_info_by_idx {{모델_타입/모델_조회_인덱스}}`

- 이름으로 모델 정보 조회:

`tts --model_info_by_name {{모델_타입/언어/데이터셋/모델_이름}}`

- 기본 보코더 모델로 텍스트를 음성으로 변환:

`tts --text "{{텍스트}}" --model_name {{모델_타입/언어/데이터셋/모델_이름}}`

- 사용자 정의 텍스트 음성 변환 모델 실행 (Griffin-Lim 보코더 사용):

`tts --text "{{텍스트}}" --model_path {{경로/대상/모델.pth}} --config_path {{경로/대상/설정.json}} --out_path {{경로/대상/파일.wav}}`
