a, b, k = gets.split().map {|i| i = i.to_i}

if a >= k
    a -= k
elsif b - (k-a) >= 0
    b -= k-a
    a = 0
else
    a, b = 0, 0
end

puts "#{a} #{b}"
