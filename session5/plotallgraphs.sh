#!/bin/bash

# shell script to generate a PDF file with sample graphs
# ./plotallgraphs.sh in terminal to run the script

for i in $( ls *.gv ); do
    echo item: $i
    dot -Tpdf $i >$i.pdf
    dot -Tpng $i >$i.png
done
