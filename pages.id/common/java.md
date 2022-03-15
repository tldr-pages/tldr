# java

> Peluncur Aplikasi Java.
> Informasi lebih lanjut: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html>.

- Menjalankan berkas java `.class` yang mengandung method main dengan hanya menggunakan nama class:

`java {{nama_class}}`

- Menjalankan program `.jar`:

`java -jar {{nama_berkas.jar}}`

- Menjalankan program `.jar` dengan menunggu debugger terhubung ke port 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{nama_berkas.jar}}`

- Menampilkan versi JDK, JRE dan HotSpot:

`java -version`

- Menampilkan informasi penggunaan untuk perintah java:

`java -help`
