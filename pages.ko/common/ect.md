# ect

> 효율적인 압축 도구.
> C++로 작성된 파일 최적화 프로그램. PNG, JPEG, gzip 및 Zip 파일을 지원.
> 더 많은 정보: <https://github.com/fhanau/Efficient-Compression-Tool>.

- 파일 압축:

`ect {{경로/대상/파일.png}}`

- 지정된 압축 수준 및 멀티스레딩을 사용하여 파일을 압축 (1=가장 빠름 (가장 안 좋음), 9=가장 느림 (가장 좋음), 기본값은 3):

`ect -{{9}} --mt-deflate {{경로/대상/파일.zip}}`

- 디렉토리의 모든 파일을 재귀적으로 압축:

`ect -recurse {{경로/대상/디렉터리}}`

- 원래 수정 시간을 유지하며, 파일을 압축:

`ect -keep {{경로/대상/파일.png}}`

- 파일을 압축하고 메타데이터를 제거:

`ect -strip {{경로/대상/파일.png}}`
