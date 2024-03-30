# bedtools

> A swiss-army knife of tools for genomic-analysis tasks.
> Used to intersect, group, convert and count data in BAM, BED, GFF/GTF, VCF format.
> More information: <https://bedtools.readthedocs.io>.

- Intersect file [a] and file(s) [b] regarding the sequences' [s]trand and save the result to a specific file:

`bedtools intersect -a {{path/to/file_A}} -b {{path/to/file_B1 path/to/file_B2 ...}} -s > {{path/to/output_file}}`

- Intersect two files with a [l]eft [o]uter [j]oin, i.e. report each feature from `file1` and NULL if no overlap with `file2`:

`bedtools intersect -a {{path/to/file1}} -b {{path/to/file2}} -loj > {{path/to/output_file}}`

- Using more efficient algorithm to intersect two pre-sorted files:

`bedtools intersect -a {{path/to/file1}} -b {{path/to/file2}} -sorted > {{path/to/output_file}}`

- [g]roup a file based on the first three and the fifth [c]olumn and apply the sum [o]peration on the sixth column:

`bedtools groupby -i {{path/to/file}} -c 1-3,5 -g 6 -o sum`

- Convert bam-formatted [i]nput file to a bed-formatted one:

`bedtools bamtobed -i {{path/to/file.bam}} > {{path/to/file.bed}}`

- Find for all features in `file1.bed` the closest one in `file2.bed` and write their [d]istance in an extra column (input files must be sorted):

`bedtools closest -a {{path/to/file1.bed}} -b {{path/to/file2.bed}} -d`
