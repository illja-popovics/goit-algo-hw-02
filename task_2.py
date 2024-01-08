from collections import deque

def is_palindrome(input_str):
    processed_str = ''.join(input_str.lower().split())
    processed_str = ''.join(char for char in processed_str if char not in [".", ",", ":", "!"]) # видалити знаки пунктуації

    char_queue = deque(processed_str)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True

# Приклад:
input_string = "Eine güldne, gute Tugend: Lüge nie!"
result = is_palindrome(input_string)

if result:
    print(f'Рядок "{input_string}" є паліндромом.')
else:
    print(f'Рядок "{input_string}" не є паліндромом.')
