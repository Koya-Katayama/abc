# 00.rbの方が速いが、普通に定義通り全部調べるのでも間に合う。回答の速さを競うコンテスト的にはこっちの方がいいのかもしれない。

x = gets.to_i

while true
    flag = true
    for i in 2..x-1
        if x % i == 0
            flag = false
            break
        end
    end
    if flag
        puts x
        break
    end
    x += 1
end
