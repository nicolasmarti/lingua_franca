function fibonacci(n::Int64)
    if n == 0
        return 0
    elseif n == 1
        return 1
    else
        a = 0
        b = 1
        while n > 0
            b = a + b
            a = b
            n -= 1
        end
        return a
    end
end
