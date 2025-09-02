def faktorial(n):
    if n < 0:
        return "input harus bilangan bulat non-negatif."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

try:
    user_input = int(input("Masukkan bilangan bulat non-negatif: "))
    result = faktorial(user_input)
    print(f"Faktorial dari {user_input} adalah: {result}")
except ValueError:
    print("input tidak valid. Harap masukkan bilangan bulat.")
