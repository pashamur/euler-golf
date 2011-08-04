perl -anF, -e 'for(sort@F){$s+=(unpack("%32W*")+60-64*length)*++$i}print $s;' names.txt
