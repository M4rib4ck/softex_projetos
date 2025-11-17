def primo(n):
    if n < 2:
        return False
    i = 2
    while i <= n//2:
        if n % i == 0:
            return False
        i += 1
    return True

num = int(input("Número: "))
print("É primo?", primo(num))
