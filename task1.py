def find_min_max(arr):
    # Базовий випадок: один елемент
    if len(arr) == 1:
        return (arr[0], arr[0])

    # Базовий випадок: два елементи
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return (arr[0], arr[1])
        else:
            return (arr[1], arr[0])

    # Рекурсивний випадок: розділяємо масив
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об'єднуємо результати
    return (min(left_min, right_min), max(left_max, right_max))


# Приклад використання
arr = [3, 5, -10, 9, 2, 8, 4]
result = find_min_max(arr)
print(f"Мінімум: {result[0]}, Максимум: {result[1]}")
