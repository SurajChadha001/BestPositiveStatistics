import threading
def worker(name):
  print(f"Worker{name}started")
  for i in range(3):
    print(f"Worker{name} doing some work-{i}")
    print(f"Worker{name}finished")
    threads=[]
    for i in range(2):
      thread=threading.Thread(target=worker,args=(f"Thread-{i+1}",))
      threads.append(thread)
      thread.start()
      for thread in threads:
        thread.join()
        print("All workers finished!")