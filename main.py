from fastapi import FastAPI
from src  import predictor 

app=FastAPI()

@app.get('/')
def root_page(avg_time:float,taken_quiz:float,exam_quiz:int,hub_quiz:float):
    result = predictor.predict(avg_time,taken_quiz,exam_quiz,hub_quiz)
    data = result
    return {'verdict': data}