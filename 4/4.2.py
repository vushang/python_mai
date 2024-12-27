import itertools


def infinite_number_generator():
    for number in itertools.count(start=1, step=1):
        yield number


def apply_function_to_iterator(iterator, func):
    for item in iterator:
        try:
            result = func(item)
            print(f"Применение функции к {item}: {result}")
        except Exception as e:
            print(f"Ошибка при обработке элемента {item}: {e}")


def combine_iterators(*iterators):
    try:
        combined_iterator = itertools.chain(*iterators)
        for item in combined_iterator:
            print(f"Объединенный элемент: {item}")
    except Exception as e:
        print(f"Ошибка при объединении итераторов: {e}")

print("Бесконечный генератор чисел:")
generator = infinite_number_generator()
for _ in range(10):
    print(next(generator))

print("\nПрименение функции к каждому элементу в итераторе:")
iterator = [1, 2, 3, "a", 5]
apply_function_to_iterator(iterator, lambda x: x * 2)

print("\nОбъединение нескольких итераторов:")
iter1 = [1, 2, 3]
iter2 = ["a", "b", "c"]
iter3 = [4, 5, 6]
combine_iterators(iter1, iter2, iter3)

print("\nОбработка исключения при объединении итераторов:")
combine_iterators(iter1, None, iter3)