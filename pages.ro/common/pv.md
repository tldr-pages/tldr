# pv

> Monitorizați progresul datelor printr-o conductă.

- Imprimați conținutul fișierului și afișați o bară de progres:

`pv {{file}}`

- Măsurați viteza și cantitatea fluxului de date între țevi (`-s` este opțional):

`command1 | pv -s {{expected_amount_of_data_for_eta}} | command2`

- Filtrați un fișier, vedeți atât progresul, cât și cantitatea de date de ieșire:

`pv -cN in {{big_text_file}} | grep {{pattern}} | pv -cN out > {{filtered_file}}`

- Atașați la un proces care rulează deja și vedeți progresul său de citire a fișierelor:

`pv -d {{PID}}`

- Citiți un fișier eronat, omiteți erorile ca `dd conv=sync, noerror` ar:

`pv -EE {{path/to/faulty_media}} > image.img`

- Opriți citirea după citirea cantității specificate de date, limita ratei la 1K/s:

`pv -L 1K -S {{maximum_file_size_to_be_read}}`
