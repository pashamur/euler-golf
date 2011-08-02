#!/usr/bin/ruby

lines = File.readlines("triangle.txt").reverse
elems = []
lines.each{|l| elems << l.split.map(&:to_i)}
1.upto(lines.length-1){|i|
	elems[i].each_index{|j|
		elems[i][j] += elems[i-1].slice(j, 2).max
	}
}
p elems[lines.length-1][0]
