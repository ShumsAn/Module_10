import multiprocessing
import datetime
def read_info(name):
    all_data = []
    with open(name,'r',encoding='utf-8') as file:
        while True:
            content = file.readline()
            all_data.append(content)
            if not content:
                break


filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

# #  Линейный вызов
# start_line = datetime.datetime.now()
# for name in filenames:
#     read_info(name)
# end_line = datetime.datetime.now()
# print(end_line - start_line)


# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start_pool = datetime.datetime.now()
        pool.map(read_info, filenames)

    end_pool = datetime.datetime.now()
    print(end_pool - start_pool)
