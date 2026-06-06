function fibonacci(n::Int)
    n < 0 && throw(ArgumentError("n doit être positif"))
    if n == 0 || n == 1
        return n
    end
    return fibonacci(n - 1) + fibonacci(n - 2)
end
