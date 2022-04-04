from celery import Celery
import time
app = Celery("templateGenerate", 
        broker="pyamqp://guest@localhost//", 
        backend="rpc://",)

@app.task
def add(x, y):
    time.sleep(20)
    return x + y