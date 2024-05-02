# compseq

> Calculate the composition of unique words in sequences.
> More information: <https://www.bioinformatics.nl/cgi-bin/emboss/help/compseq/>.

- Count observed frequencies of words in a FASTA file, providing parameter values with interactive prompt:

`compseq {{example.fasta}}`

- Count observed frequencies of amino acid pairs from a FASTA file, save output to a text file:

`compseq {{example_protein.fasta}} -word 2 {{result1.comp}}`

- Count observed frequencies of hexanucleotides from a FASTA file, save output to a text file and ignore zero counts:

`compseq {{example_dna.fasta}} -word 6 {{result2.comp}} -nozero`

- Count observed frequencies of codons in a particular reading frame; ignoring any overlapping counts (i.e. move window across by word-length 3):

`compseq -sequence {{example_rna.fasta}} -word 3 {{result3.comp}} -nozero -frame {{1}}`

- Count observed frequencies of codons frame-shifted by 3 positions; ignoring any overlapping counts (should report all codons except the first one):

`compseq -sequence {{example_rna.fasta}} -word 3 {{result4.comp}} -nozero -frame 3`

- Count amino acid triplets in a FASTA file and compare to a previous run of `compseq` to calculate expected and normalised frequency values:

`compseq -sequence {{human_proteome.fasta}} -word 3 {{result5.comp}} -nozero -infile {{prev.comp}}`

- Approximate the above command without a previously prepared file, by calculating expected frequencies using the single base/residue frequencies in the supplied input sequence(s):

`compseq -sequence {{human_proteome.fasta}} -word 3 {{result6.comp}} -nozero -calcfreq`

- Display help (use `-help -verbose` for more information on associated and general qualifiers):

`compseq -help`
