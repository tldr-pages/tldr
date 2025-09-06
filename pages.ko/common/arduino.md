# arduino

> Arduino Studio - Arduino 플랫폼을 위한 통합 개발 환경.
> 더 많은 정보: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- 스케치 작성:

`arduino --verify {{경로/대상/파일.ino}}`

- 스케치를 작성하고 업로드:

`arduino --upload {{경로/대상/파일.ino}}`

- Atmega328p CPU가 장착된 Arduino Nano에 스케치를 빌드하고 업로드, 포트 `/dev/ttyACM0`에 연결됨:

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{경로/대상/파일.ino}}`

- 환경 설정 `name`을 주어진 `value`로 설정:

`arduino --pref {{이름}}={{값}}`

- 스케치를 빌드하고 빌드 결과를 빌드 디렉터리에 넣고, 해당 디렉토리에 있는 이전 빌드 결과를 재사용:

`arduino --pref build.path={{경로/대상/빌드_디렉터리}} --verify {{경로/대상/파일.ino}}`

- (변경된) 기본 설정을 `preferences.txt`에 저장:

`arduino --save-prefs`

- 최신 SAM 보드 설치:

`arduino --install-boards "{{arduino:sam}}"`

- Bridge 및 Servo 라이브러리 설치:

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`
