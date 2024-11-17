import threading
class mythread(threading.Thread):
    def run(self):
        print("this is thread")
thread=mythread()
thread.start()

class myclass():
    def run(self):
        print("run method")
ob=myclass()
ob.run()