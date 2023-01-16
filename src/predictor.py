import pickle
import numpy as np
import pandas as pd


def predict(avg_time,taken_quiz,exam_quiz,hub_quiz):
    model =pickle.load(open('models/logistic.pkl','rb'))
    val=np.array([avg_time,taken_quiz,exam_quiz,hub_quiz])
    churn = model.predict(val.reshape(1,-1))
    if churn == 1:
        verdict ="Student will convert to paid course"
        return verdict
    else:
        verdict = "student will not convert to paid course" 
        return verdict

if __name__ == '__main__':
    res = predict(0,1,0,0)
    print(res)