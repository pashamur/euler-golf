class Fraction
  attr_accessor :num, :den, :gcd

  def initialize(num, den)
    @num = num            # numerator
    @den = den            # denominator
    @gcd = gcd(num, den)  # greatest common factor (num, den)
  end

  def equals(other)
    (self.simplified.num == other.simplified.num and self.simplified.den == other.simplified.den)
  end

  def times(other)
    Fraction.new(@num*other.num, @den*other.den)
  end

  def to_s
    @num.to_s + "/" + @den.to_s
  end

  def simplified
    Fraction.new(@num/@gcd, @den/@gcd)
  end

  def interesting
    ((@num%10 != @num/10) and (@den/10 != @den%10) and (@num%10 == @den/10))
  end

  def gcd(a, b)
    return gcd(b, a) if a < b

    x = a.to_i
    y = b.to_i

    while y != 0
        r = x % y
        x = y
        y = r
    end

    return x
  end
end


def generate_fractions_brute_force
  product = Fraction.new(1,1)
  (10..99).each do |n|
    (10..99).each do |m|
      fraction = Fraction.new(n,m)
      if fraction.interesting and fraction.equals(Fraction.new(n/10, m%10))
        puts "Digit cancelling fraction: " + fraction.to_s
        product = product.times(fraction)
      end
    end
  end
  puts "Product of fractions: " + product.to_s
  puts "Simplified product: "   + product.simplified.to_s
end

generate_fractions_brute_force