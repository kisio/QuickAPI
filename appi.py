from fastapi import FastAPI

app=FastAPI()

richest_people_list={
    'elon musk':'300 billion USD',
    'Derrick Kisio':'200 billion USD',
    ' Jeff Bezos':'100 billion USD',
    'Mark Zuck':'150 billion USD'
}

@app.get('/richest-people')
def richest_people():
    return richest_people_list