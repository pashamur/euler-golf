ruby -anF, -e 's=0;$F.sort.map{|w|w[1..-2].bytes{|c|s+=$.*(c-?@)};$.+=1};p s' names.txt
