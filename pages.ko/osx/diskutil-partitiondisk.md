# diskutil partitionDisk

> 디스크 및 볼륨 내 파티션을 관리하는 도구.
> `diskutil`의 일부.
> APM은 macOS에서만 지원되고, MBR은 DOS에 최적화되어 있으며, GPT는 대부분의 최신 시스템과 호환됩니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- APM/MBR/GPT 파티션 방식을 사용하여 볼륨을 다시 포맷하고 안의 모든 파티션을 삭제 (볼륨의 모든 데이터가 지워집니다):

`diskutil partitionDisk {{/dev/디스크_장치}} 0 {{APM|MBR|GPT}}`

- 볼륨을 다시 포맷한 후, 모든 여유 공간을 사용하는 특정 파일 시스템으로 단일 파티션 생성:

`diskutil partitionDisk {{/dev/디스크_장치}} 1 {{APM|MBR|GPT}} {{파티션_파일시스템}} {{파티션_이름}}`

- 볼륨을 다시 포맷한 후, 특정 크기 이하로 단일 파티션 생성 (예: `16G`는 16GB, `50%`는 전체 볼륨 크기의 절반):

`diskutil partitionDisk {{/dev/디스크_장치}} 1 {{APM|MBR|GPT}} {{파티션_파일시스템}} {{파티션_이름}} {{파티션_크기}}`

- 볼륨을 다시 포맷한 후, 여러 파티션 생성:

`diskutil partitionDisk {{/dev/디스크_장치}} {{파티션_수}} {{APM|MBR|GPT}} {{파티션_파일시스템1}} {{파티션_이름1}} {{파티션_크기1}} {{파티션_파일시스템2}} {{파티션_이름2}} {{파티션_크기2}} ...`

- 파티션을 위한 모든 지원 파일 시스템 나열:

`diskutil listFilesystems`
