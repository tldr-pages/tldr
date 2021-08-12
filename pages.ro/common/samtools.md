# samtools

> Instrumente pentru manipularea datelor de secvențiere cu debit mare (genomică).
> Folosit pentru citirea/scrierea/editarea/indexarea/vizualizarea datelor în format SAM/BAM/CRAM.

- Convertiți un fișier de intrare SAM în flux BAM și salvați în fișier:

`samtools view -S -b {{input.sam}} > {{output.bam}}`

- Ia de intrare de la stdin (-) și imprimați antetul SAM și orice citește care se suprapun o anumită regiune la stdout:

`{{other_command}} | samtools view -h - chromosome:start-end`

- Sortați fișierul și salvați la BAM (formatul de ieșire este determinat automat din extensia fișierului de ieșire):

`samtools sort {{input}} -o {{output.bam}}`

- Index un fișier BAM sortat (creează {{sorted_input.bam.bai}}):

`samtools index {{sorted_input.bam}}`

- Se imprimă statistici de aliniere despre un fișier:

`samtools flagstat {{sorted_input}}`

- Contorizarea alinierilor la fiecare indice (cromozom/contig):

`samtools idxstats {{sorted_indexed_input}}`

- Îmbinați mai multe fișiere:

`samtools merge {{output}} {{input1 input2 …}}`

- Împărțiți fișierul de intrare în funcție de grupurile de citire:

`samtools split {{merged_input}}`
