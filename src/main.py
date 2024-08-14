from fastapi import FastAPI


app = FastAPI(title='CI/CD - Example')

@app.get('/')
async def say_hello() -> str:
    return 'Hello =)'


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8080)