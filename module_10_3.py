import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break



if __name__ == '__main__':
    file_names = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
    #start_time = time.time()
    #for file_name in file_names:
        #read_info(file_name)  # Вызываем функцию для каждого файла
    #print(f"Линейный вызов занял по времени: {time.time() - start_time:.4f} секунд")

# Многопроцессный
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, file_names)
    print(f"Многопроцессный занял по времени: {time.time() - start_time:.4f} секунд")

