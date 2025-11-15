# asr

> 디스크 이미지를 볼륨에 복원(복사)합니다.
> 명령어 이름은 Apple Software Restore를 의미합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/asr.8.html>.

- 디스크 이미지를 대상 볼륨에 복원:

`sudo asr restore --source {{이미지_파일.dmg}} --target {{경로/대상/볼륨_파일}}`

- 복원하기 전에 대상 볼륨 지우기:

`sudo asr restore --source {{이미지_파일.dmg}} --target {{경로/대상/볼륨_파일}} --erase`

- 복원 후 검증 건너뛰기:

`sudo asr restore --source {{이미지_파일.dmg}} --target {{경로/대상/볼륨_파일}} --noverify`

- 중간 디스크 이미지를 사용하지 않고 볼륨 복제:

`sudo asr restore --source {{경로/대상/볼륨_파일}} --target {{경로/대상/볼륨_파일}}`
