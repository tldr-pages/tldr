# cvfsck

> Xsan 파일시스템 볼륨을 검사하고 복구하는 도구.
> macOS의 Xsan 파일시스템 유틸리티에 포함됨.
> 더 많은 정보: <https://www.manpagez.com/man/1/cvfsck/>.

- Xsan 볼륨의 메타데이터 손상 여부 검사 (읽기 전용):

`sudo cvfsck {{/Volumes/XsanVolume}}`

- 손상된 Xsan 볼륨 복구 (문제 수정):

`sudo cvfsck -w {{/Volumes/XsanVolume}}`

- 문제를 시스템 로그에 기록 (주로 자동 시작 시 검사에서 사용됨):

`sudo cvfsck -l {{/Volumes/XsanVolume}}`

- Xsan 볼륨의 여유 공간 단편화 상태 보고:

`sudo cvfsck -f {{/Volumes/XsanVolume}}`
