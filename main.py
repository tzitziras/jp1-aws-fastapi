from fastapi import FastAPI, Request
from textblob import TextBlob
from pydantic import BaseModel
import json

app = FastAPI()


class InputText(BaseModel):
    text: str


def sentiment_score(text: str) -> int:
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    # Normalize the sentiment to a 1-10 scale
    score = int((sentiment + 1) * 4.5) + 1
    return score


@app.post("/sentiment")
async def get_sentiment(input_text: InputText):
    score = sentiment_score(input_text.text)
    return {"sentiment_score": score}


@app.get("/")
async def read_root(request: Request):
    #my_body = await request.body()
    #return my_body
    client_host = request.client.host
    #my_path = request['path']
    #return my_path
    #client = json.dumps(request.client)
    #return client
    return {"message": "Hello World - jp2", "client_host": client_host}
