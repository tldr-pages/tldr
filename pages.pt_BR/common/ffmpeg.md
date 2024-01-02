# ffmpeg

> Ferramenta de conversão de vídeo.
> Mais informações: <https://ffmpeg.org>.

- Extrai o som de um vídeo e salva-o como MP3:

`ffmpeg -i {{caminho/para/vídeo.mp4}} -vn {{caminho/para/som}}.mp3`

- Converte quadros de um vídeo ou GIF para imagens numeradas individuais:

`ffmpeg -i {{vídeo|gif}} {{quadro_%d.png}}`

- Combina imagens numeradas (`quadro_1.jpg`, `quadro_2.jpg`, etc) em um vídeo ou GIF:

`ffmpeg -i {{caminho/para/quadro_%d.jpg}} -f image2 {{vídeo|gif}}`

- Extrai um único quadro de um vídeo no tempo mm:ss e o salva como uma imagem de resolução 128x128:

`ffmpeg -ss {{mm:ss}} -i {{caminho/para/vídeo.mp4}} -frames 1 -s {{128x128}} -f image2 {{caminho/para/quadro.png}}`

- Corta um vídeo de um dado tempo inicial mm:ss até um tempo final mm2:ss2 (omita a opção -to para cortar o vídeo até o final):

`ffmpeg -ss {{mm:ss}} -to {{mm2:ss2}} -i {{caminho/para/vídeo_entrada.mp4}} -codec copy {{caminho/para/vídeo_saída.mp4}}`

- Converte um vídeo AVI para MP4. AAC Áudio @ 128kbit, h264 Vídeo @ CRF 23:

`ffmpeg -i {{caminho/para/vídeo_entrada}}.avi -codec:a aac -b:a 128k -codec:v libx264 -crf 23 {{caminho/para/vídeo_saída}}.mp4`

- Remixa um vídeo MKV para MP4 sem recodificar áudio ou vídeo:

`ffmpeg -i {{caminho/para/vídeo_entrada}}.mkv -codec copy {{caminho/para/vídeo_saída}}.mp4`

- Converte um vídeo MP4 para o codec VP9. Para a melhor qualidade, use um valor CRF (faixa recomendada 15-35) e -b:v DEVE ser 0:

`ffmpeg -i {{caminho/para/vídeo_entrada}}.mp4 -codec:v libvpx-vp9 -crf {{30}} -b:v 0 -codec:a libopus -vbr on -threads {{número_de_threads}} {{caminho/para/vídeo_saída}}.webm`
