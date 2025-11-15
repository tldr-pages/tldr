# drutil

> DVD 버너와 상호 작용.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/drutil.1.html>.

- 드라이브에서 디스크 배출:

`drutil eject`

- 디렉토리를 ISO9660 파일 시스템으로 DVD에 굽기. 검증하지 않고 완료 시 배출:

`drutil burn -noverify -eject -iso9660`
