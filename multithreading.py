import threading
import time

def thread_function(name,i):
	print(name)
	s=time.time()
	print("starting threadfor i: ",i)
	print("Start process for i: "+str(i))
	time.sleep(7)
	print("processing for i: "+str(i)+"done!")
	print("finishing thread for i: ", i)
	e=time.time()
	print("time for threaded process(start,end,total): ",s,e,s-e)


if __name__ == "__main__":
	i=0
	while(i<10):
		start=time.time()
		print("i: ",i)
		print("processing ",i)
		time.sleep(5)
		print("finished processing ",i)
		nm="chandan"
		x = threading.Thread(target=thread_function, args=(nm,i))
		x.start()
		i=i+1
		end=time.time()
		print("time for main process(start,end,total): ",start,end,start-end)
