# java

> Java アプリケーションランチャ。
> もっと詳しく: <https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html>。

- main メソッドを含む Java の `.class` ファイルを、クラス名だけで実行する:

`java {{クラス名}}`

- Java プログラムを実行し、追加のサードパーティまたはユーザー定義クラスを使用する:

`java -classpath {{path/to/classes1}}:{{path/to/classes2}}:. {{クラス名}}`

- `.jar` プログラムを実行する:

`java -jar {{filename.jar}}`

- `.jar` プログラムを、デバッグ待ちポート 5005 で実行する:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- JDK、JRE、HotSpot のバージョンを表示する:

`java -version`

- ヘルプを表示する:

`java -help`
