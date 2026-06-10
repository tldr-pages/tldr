# jp2a

> Փոխարկել JPEG պատկերները ASCII-ի:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/jp2a>:.

- Կարդացեք JPEG պատկերը ֆայլից և տպեք ASCII-ով:

`jp2a {{path/to/image.jpeg}}`

- Կարդացեք JPEG պատկերը URL-ից և տպեք ASCII-ով.:

`jp2a {{www.example.com/image.jpeg}}`

- Գունավորեք ASCII ելքը.:

`jp2a --colors {{path/to/image.jpeg}}`

- Նշեք նիշերը, որոնք պետք է օգտագործվեն ASCII ելքի համար.:

`jp2a --chars='{{..-ooxx@@}}' {{path/to/image.jpeg}}`

- Գրեք ASCII ելքը ֆայլի մեջ.:

`jp2a --output={{path/to/output_file.txt}} {{path/to/image.jpeg}}`

- Գրեք ASCII ելքը HTML ֆայլի ձևաչափով, որը հարմար է վեբ բրաուզերներում դիտելու համար.:

`jp2a --html --output={{path/to/output_file.html}} {{path/to/image.jpeg}}`
