# yolo

> YOLO 명령줄 인터페이스는 다양한 작업과 버전에서 모델을 간단하게 학습, 검증 또는 추론할 수 있게 해줍니다.
> 더 많은 정보: <https://docs.ultralytics.com/cli/>.

- 현재 작업 디렉토리에 기본 설정의 복사본 생성:

`yolo task=init`

- 지정된 설정 파일로 객체 탐지, 인스턴스 분할, 또는 분류 모델 학습:

`yolo task={{detect|segment|classify}} mode=train cfg={{경로/대상/config.yaml}}`
