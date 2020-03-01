#!/bin/bash
for i in 1 2 2a 3 4 5 6 7 8
do
    cp /courses/TSKS11/ht2019/data_and_fcns/session3/task1/_g$i.edges _G.edges
    ./analysis
    cp _G-degree.csv _G-degree-$i.csv
    cp _G-clustering.csv _G-clustering-$i.csv
done    
        
