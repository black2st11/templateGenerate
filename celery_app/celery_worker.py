from time import sleep

from celery import current_task

from .celery import app


@app.task(name='test_celery')
def test_celery(word: str) -> str:
    # for i in range(1, 11):
    #     current_task.update_state(state='PROGRESS',
    #                               meta={'process_percent': i*10})
    return f"test task return {word}"