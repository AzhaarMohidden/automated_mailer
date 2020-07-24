import concurrent.futures
import time
from tqdm.auto import tqdm
# total=0
# def smth():
#     for l in tqdm(range(100)):
#         time.sleep(0.02)
#         pass
# def tq():
#     pbar = tqdm(total= 100)
#     for i in range(100):
#         time.sleep(0.02)
#         pbar.update(1)
# def slp():
#     print("doing something")
#     time.sleep(2)

# def cnt(ret_value):
#     v = 0
#     global total1
#     for i in range(50000000):
#         v = v+i
#     ret_value.value = v
#
# def cnt2(ret1_value):
#     d = 0
#     global total2
#     for i in range(50000000):
#         d = d+i
#     ret1_value.value = d


# cnt()
# cnt2()
# gtotal = total1+ total2
# print(gtotal)
# ret_value = multiprocessing.Value("i", 0.0, lock=False)
# ret1_value = multiprocessing.Value("i", 0.0, lock=False)
# p1 = multiprocessing.Process(target=cnt, args= ret_value)
# p2 = multiprocessing.Process(target=cnt2, args= ret1_value)
#
# #
# pr = []
# if __name__ == '__main__':
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print(ret_value)
#     print(ret1_value)
#     p1.start()
#     p2.start()
# with tqdm(total = 100) as pbar:
#     for i in range(10):
#         pbar.update()
#         sleep(1)
#         pbar.update()
#         sleep(2)
#         pbar.update()
#         sleep(4)
#         pbar.update()
#         sleep(0.5)

def dometh3():
    c = 0
    for f in range(10000):
        c = c+f
    return c

def dometh():
    c = 0
    for f in range(0, 5000, 1):
        c = c+f
    return c


def dometh2():
    v = 0
    for i in range(501, 5000, 1):
        v = v+i
    return v

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1= executor.submit(dometh)
        f2= executor.submit(dometh2)

        print(f1.result())
        print(f2.result())
        print("*************************")
        print(f1.result()+f2.result())
        print("*************************")
        print(dometh3())
