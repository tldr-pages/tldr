# mmdc

> CLI ջրահարսի համար, դիագրամի ստեղծման գործիք՝ տիրույթին հատուկ լեզվով:.
> Ջրահարսի սահմանման ֆայլը ընդունվում է որպես մուտքագրում, իսկ SVG, PNG կամ PDF ֆայլը ստեղծվում է որպես ելք:.
> Լրացուցիչ տեղեկություններ. <http://mermaid.js.org/>:.

- Փոխակերպեք ֆայլը նշված ձևաչափին (ավտոմատ կերպով որոշվում է ֆայլի ընդլայնումից).:

`mmdc {{[-i|--input]}} {{input.mmd}} {{[-o|--output]}} {{output.svg}}`

- Նշեք գծապատկերի թեման.:

`mmdc {{[-i|--input]}} {{input.mmd}} {{[-o|--output]}} {{output.svg}} {{[-t|--theme]}} {{forest|dark|neutral|default}}`

- Նշեք գծապատկերի ֆոնի գույնը (օրինակ՝ `lime`, `"#D8064F"` կամ `transparent`):

`mmdc {{[-i|--input]}} {{input.mmd}} {{[-o|--output]}} {{output.svg}} {{[-b|--backgroundColor]}} {{color}}`
