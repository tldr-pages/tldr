# transcode

> Transcodificați codecurile video și audio și convertiți între formate media.

- Creați fișier de stabilizare pentru a putea elimina shake-urile camerei:

`transcode -J stabilize -i {{input_file}}`

- Eliminați shake-urile camerei după crearea fișierului de stabilizare, transformați video folosind xvid:

`transcode -J transform -i {{input_file}} -y xvid -o {{output_file}}`

- Redimensionați videoclipul la 640x480 pixeli și convertiți la codec MPEG4 folosind xvid:

`transcode -Z 640x480 -i {{input_file}} -y xvid -o {{output_file}}`
