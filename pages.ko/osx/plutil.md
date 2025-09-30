# plutil

> 속성 목록("plist") 파일을 보기, 변환, 검증 또는 편집.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/plutil.1.html>.

- 하나 이상의 plist 파일 내용을 사람이 읽을 수 있는 형식으로 표시:

`plutil -p {{파일1.plist 파일2.plist ...}}`

- 하나 이상의 plist 파일을 XML 형식으로 변환하여 원본 파일을 덮어쓰기:

`plutil -convert xml1 {{파일1.plist 파일2.plist ...}}`

- 하나 이상의 plist 파일을 바이너리 형식으로 변환하여 원본 파일을 덮어쓰기:

`plutil -convert binary1 {{파일1.plist 파일2.plist ...}}`

- plist 파일을 다른 형식으로 변환하여 새 파일에 쓰기:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{경로/대상/파일.plist}} -o {{경로/대상/새_파일.plist}}`

- plist 파일을 다른 형식으로 변환하여 `stdout`에 쓰기:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{경로/대상/파일.plist}} -o -`
