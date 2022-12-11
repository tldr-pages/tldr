# java

> Peluncur Aplikasi Java.
> Informasi lebih lanjut: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/java.html>.

- Jalankan berkas java `.class` yang mengandung method main dengan hanya menggunakan nama class:

`java {{nama_class}}`

- Jalankan sebuah program java menggunakan berkas-berkas `.class` eksternal dan tambahan:

`java -classpath {{jalan/menuju/direktori_class1}}:{{jalan/menuju/direktori_class2}}:. {{nama_class}}`

- Jalankan program `.jar`:

`java -jar {{nama_berkas.jar}}`

- Jalankan program `.jar` dengan menunggu debugger terhubung ke port 5005:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{nama_berkas.jar}}`

- Tampilkan versi JDK, JRE dan HotSpot:

`java -version`

- Tampilkan informasi penggunaan untuk perintah java:

`java -help`
