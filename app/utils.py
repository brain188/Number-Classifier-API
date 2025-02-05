def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
            return sum == n

def is_armstrong(n):
    n = abs(n)
    digits = [int(d) for d in str(n)]
    return sum([d ** len(digits) for d in digits]) == n

def get_fun_fact(n):
    import requests
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=2)
        return response.text if response.status_code == 200 else "No fact available"
    except requests.exceptions.RequestException:
        return "No fact Available"
    
def classify_number(n):
    properties = []
    if n % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")
    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    if is_armstrong(n):
        properties.append("armstrong")
    
    return properties