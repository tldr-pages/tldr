# nmap

> Alat penjelajah jaringan komputer dan pemindai keamanan/port jaringan komputer.
> Beberapa fitur (seperti pemindaian SYN) hanya aktif jika `nmap` dijalankan menggunakan hak istimewa pengguna root.
> Lihat juga: `hping3`, `masscan`, `naabu`, `rustscan`, `zmap`.
> Informasi lebih lanjut: <https://nmap.org/book/man.html>.

- Pindai 1000 port paling umum untuk suatu host jarak jauh dengan menentukan tingkat perincian ([v]erbosity) log pemindaian:

`nmap -v{{1|2|3}} {{ip_atau_hostname}}`

- Jalankan serangan sapuan ping (ping sweep) secara sangat agresif terhadap suatu [s]ub[n]et atau kumpulan host individu:

`nmap -T5 -sn {{192.168.0.0/24|ip_atau_hostname1,ip_atau_hostname2,...}}`

- Nyalakan fitur deteksi sistem operasi, deteksi sistem, pemindaian naskah, dan jejak traceroute atas kumpulan host dari suatu berkas:

`sudo nmap -A -iL {{jalan/menuju/berkas.txt}}`

- Pindai kumpulan host terhadap kumpulan [p]ort tertentu (gunakan `-p-` untuk seluruh port dari 1 hingga 65535):

`nmap -p {{port1,port2,...}} {{ip_atau_host1,ip_atau_host2,...}}`

- Lakukan proses deteksi layanan dan versi terhadap 1000 port paling umum menggunakan naskah NSE bawaan, tuliskan luaran program (`-oA`) ke dalam berkas-berkas baru berawalan nama tertentu:

`nmap -sC -sV -oA {{top-1000-ports}} {{ip_atau_host1,ip_atau_host2,...}}`

- Periksa kumpulan target secara hati-hati menggunakan skrip NSE `default and safe`:

`nmap --script "default and safe" {{ip_atau_host1,ip_atau_host2,...}}`

- Pindai kumpulan peladen web yang berjalan dalam [p]ort standar 80 dan 443 menggunakan seluruh skrip NSE dengan nama yang berawalkan `http-*`:

`nmap --script "http-*" {{ip_atau_host1,ip_atau_host2,...}} -p 80,443`

- Coba hindari deteksi sistem IDS/IPS dengan memindai secara sangat perlahan (`-T0`), alamat ip sumber umpan ([D]ecoy), paket ter[f]ragmentasi, data acak, dan metode lainnya:

`sudo nmap -T0 -D {{ip_umpan1,ip_umpan1,...}} --source-port {{53}} -f --data-length {{16}} -Pn {{ip_atau_host}}`
