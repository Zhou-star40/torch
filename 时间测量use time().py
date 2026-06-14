#use time()
import time
#记录开始时间，调用time中的time记录当前时间
start_time = time.time()

#记录结束时间，调用time中的time记录当前时间
end_time = time.time()

#记录开始时间和结束时间的差值
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")

