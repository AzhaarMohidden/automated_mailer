from tqdm.auto import tqdm
from time import sleep
# # loop = tqdm(total = 5000, position = 0, leave = False)
# # for k in range(5000):
# #     loop.set_description("Loading... ".format(k))
# #     loop.update(1)
# # loop.close()
# # for i in tqdm(range(10001)):
# #     sleep(0.0001)
# #     pass
# #     print(i, end= '\r')
with tqdm(total = 100) as pbar:
    for i in range(10):
        pbar.update()
        sleep(1)
        pbar.update()
        sleep(2)
        pbar.update()
        sleep(4)
        pbar.update()
        sleep(0.5)
