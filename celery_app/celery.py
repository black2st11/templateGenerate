from celery import Celery

app = Celery("templateGenerate", 
        broker="pyamqp://guest@localhost//", 
        backend="rpc://",
        include=['test_celery']
        )


app.conf.update(result_expires=3600,)

@app.task(name='test_celery')
def test_celery(word: str) -> str:
    # for i in range(1, 11):
    #     current_task.update_state(state='PROGRESS',
    #                               meta={'process_percent': i*10})
    return f"test task return {word}"

if __name__ == "__main__":
    app.start()