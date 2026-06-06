function fib_rec(n::Int)
    n < 0 && throw(ArgumentError("n doit être positif"))
    if n == 0 || n == 1
        return n
    end
    return fib_rec(n - 1) + fib_rec(n - 2)
end
