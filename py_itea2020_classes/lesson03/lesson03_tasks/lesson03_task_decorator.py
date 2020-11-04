import time
from datetime import datetime

def decorator(repetitions=3):
    def actual_decorator(func):

        def wrapper(*args,**kwargs):
            start_time = datetime.now()
            executions_timings = []
            for i in range(repetitions):
                start_iteration_time = datetime.now()
                func_result = func(*args,**kwargs)
                end_iteration_time = datetime.now()
                iteration_duration_millisec = (end_iteration_time - start_iteration_time).microseconds/1000
                executions_timings.append(iteration_duration_millisec)
            end_time = datetime.now()
            total_time_millisec = (end_time - start_time).microseconds/1000
            return {'executions_timings_millisec': executions_timings, 'total_time_millisec': total_time_millisec, 'decorated_func_name': func.__name__, 'last_result': func_result}

        return wrapper

    return actual_decorator

@decorator(5)
def target_function(*args,**kwargs):
    time.sleep(0.050)
    if args:
        name = args[0]
    else:
        name = kwargs.get('name', 'Unknown')
    print(f'Hello world from {name}')
    return f'Hello world from {name}'


result = target_function(name='Nastya')
print(result)
