# Minecraft

> 헤드리스 Minecraft 서버 실행.
> 더 많은 정보: <https://minecraft.wiki/w/Tutorial:Setting_up_a_Java_Edition_server>.

- Minecraft 서버를 실행하며, 월드가 없으면 자동으로 생성:

`java -jar {{경로/대상/서버.jar}} --nogui`

- 서버의 최소/최대 메모리 설정 후 실행 (참고: 최소값과 최대값을 동일하게 설정하면 JVM 힙 크기 조정으로 인한 지연을 줄일 수 있습니다):

`java -Xms{{1024M}} -Xmx{{2048M}} -jar {{경로/대상/서버.jar}} --nogui`

- GUI와 함께 서버 실행:

`java -jar {{경로/대상/서버.jar}}`

- [대화형] 서버 종료:

`stop`
