
## Problems with RabbitMQ

Problems faced while using RabbitMQ: -

1) **Timeout Errors**
```
File "D:\python\Celery\app.py", line 8, in <module> print(f"Result: {result.get()}") File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\site-packages\celery\result.py", line 251, in get return self.backend.wait_for_pending( File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\site-packages\celery\backends\base.py", line 755, in wait_for_pending meta = self.wait_for( File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\site-packages\celery\backends\base.py", line 1104, in _is_disabled raise NotImplementedError(E_NO_BACKEND.strip()) NotImplementedError: No result backend is configured.
```

2) **Does not unpack the given values properly**
```
It seems like an exception is being raised when trying to get the result of the task. The error message "ValueError: not enough values to unpack (expected 3, got 0)" suggests that there might be an issue with the result returned by the task.
```

3) RabbitMQ requires ERLANG to be installed as a pre-requisite

## Redis-server

Installation of Redis-Server

### Steps

```bash
 sudo apt-add-repository ppa:redislabs/redis
 sudo apt-get update
 sudo apt-get upgrade
 sudo apt-get install redis-server
```

```bash
 sudo service redis-server restart
```

3 major files
1. `celery_config.py`
2. `tasks.py`
3. `run_task.py`

1) celery_config.py

```python
# celery_config.py
from kombu import Exchange, Queue
# Redis as the message broker and backend
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'
# Optional: Set result expiration time (in seconds)
result_expires = 3600
# Optional: Configure queues
task_queues = [
    Queue('default', Exchange('default'), routing_key='default'),
]
```

2) tasks.py

```python
# tasks.py
from celery import Celery
app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',  # Redis as the message broker
    backend='redis://localhost:6379/0'  # Redis as the result backend
)
@app.task
def add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")
    return result
  
@app.task
def mul(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result
```

3) run_task.py (worker)

```python
from tasks import mul
result = mul.delay(4, 4)
print("Task ID:", result.id)
print("Waiting for the result...")
try:
    # Wait for the result with a timeout
    result_value = result.get(timeout=10)
    print("Result:", result_value)
except Exception as e:
    print(f"Error getting result: {e}")
```

Celery run command :
```bash
celery -A tasks worker --loglevel=info
```

Worker run 
```bash
python3 run_task.py
```

### OUTPUT

![[Pasted image 20240109183728.png]]

