# MIXER

> 사운드 볼륨을 확인/설정하는 명령어.
> 더 많은 정보: <https://www.dosbox.com/wiki/MIXER>.

- 현재 볼륨 상태 출력:

`MIXER`

- 마스터 볼륨 설정 (좌:우 비율):

`MIXER master {{80}}:{{80}}`

- Sound Blaster 볼륨을 데시벨 단위로 설정:

`MIXER sb d{{10}}:d{{10}}`

- GUS 왼쪽 채널만 설정:

`MIXER gus {{50}}`

- 결과를 출력하지 않고 볼륨 설정:

`MIXER gus {{40}}:{{40}} /NOSHOW`

- 사용 가능한 MIDI 장치 목록 출력 (Windows 전용):

`MIXER /LISTMIDI`
