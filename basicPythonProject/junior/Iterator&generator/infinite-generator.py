

## test speed
import time
#
# generator_start_time = time.time()
# print(sum(n for n in range(1000000000)))
# generator_stop_time = time.time() - generator_start_time    ## generator_stop_time is 23.934149026870728
#
# list_start_time = time.time()
# print(sum([n for n in range(1000000000)]))
# list_stop_time = time.time() - list_start_time  #list_stop_time is 64.61398386955261
#
# print(f"generator_stop_time is {generator_stop_time}")
#
# print(f"list_stop_time is {list_stop_time}")

print(n for n in range(100000))    ## <generator object <genexpr> at 0x1050b0200>




