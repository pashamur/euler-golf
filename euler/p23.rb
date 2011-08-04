#!/usr/bin/ruby
def abundant_numbers(from, to)
	abundants = Array.new
	from.upto(to){|num|
		factor_sum = 0
		
		(2).upto((Math.sqrt(num)).floor){ |factor|
			if num % factor == 0 then
				if factor != Math.sqrt(num) then # if we found the square root, don't add it twice
					factor_sum += (num/factor)
				end
				factor_sum += factor
			end
		} #end factor loop
	
		if factor_sum > num then
			abundants << num
		end
	}
	return abundants
end

# populate array we'll be checking (all to 48 + only odds for >49) 
even_sums = [24,30,32,36,38,40,42,44,48] 
tocheck = *(1..22062)
# generate our abundant numbers
nums = abundant_numbers(2,22062) 
even_nums = []
odd_nums = []

# since tocheck only contains odds, we only need to sum even + odd
nums.each{|abundant|
	if abundant % 2 == 0 then
		even_nums << abundant
	else
		odd_nums << abundant
	end
}
tocheck.each_index{|i|
	if tocheck[i] % 2 == 0 and tocheck[i] > 48 then
		tocheck[i]=0
	end
}
odd_nums.each{|odd|
	even_nums.each{|even|
		tocheck[even+odd-1]=0
	}
}
tocheck = tocheck - even_sums

sum = tocheck.inject{|sum, c| if c != nil then sum + c else sum end};
print sum

