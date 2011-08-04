ruby -anF, -e 'a=[];t=0;1.upto(99){|i|a<<i*(i+1)/2};$F.sort.map{|w|s=0;w[1..-2].bytes{|c|s+=(c-?@)};a.include?(s)?t+=1:1};p t' words.txt
