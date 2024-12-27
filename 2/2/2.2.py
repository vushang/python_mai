class DataBuffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Буфер переполнен. Очистка буфера.")
            self.buffer.clear()

    def get_data(self):
        if not self.buffer:
            print("Буфер пуст. Нет данных для получения.")
            return None
        return self.buffer

buffer = DataBuffer()

buffer.add_data(1)
buffer.add_data(2)
buffer.add_data(3)
buffer.add_data(4)
buffer.add_data(5)

print(buffer.get_data())

buffer.add_data(10)
print(buffer.get_data())