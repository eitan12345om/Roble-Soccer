import time

from rq import Queue

from bg_functions import bg_job
from worker import conn

q = Queue(connection=conn)

job = q.enqueue(bg_job, "Hello there!")
print("This happens first")
time.sleep(4)
print(f"Result: {job.result}")
