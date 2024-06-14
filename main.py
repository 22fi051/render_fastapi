from typing import Optional

from fastapi import FastAPI, Form

from fastapi.responses import HTMLResponse

import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉！素晴らしい幸運が舞い込むでしょう。",
        "中吉！努力が実を結び、良い結果が待っています。",
        "小吉！ちょっとした幸運があなたの元にやってきます。",
        "吉！安定した幸せな日々が続くでしょう。",
        "半吉! まぁまぁの幸運があなたの元にやってきます。",
        "末吉！努力が実り始め、良い方向に進む時期です。",
        "末小吉! ちょっとした幸運があなたの元にやってきます。",
        "凶。悪いことが起こるかもしれませんが、気を引き締めてください。",
        "小凶。注意が必要な日です。慎重に行動しましょう。",
        "大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。"
    ]

    return {"omikuji": omikuji_list[random.randrange(10)]}

@app.post("/present")
async def circleArea(radius: float = Form(...)):
    return {"result": f"面積は{radius * radius * 3.14159}"}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <style>
                body {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                }
                h1 {
                    color: #333;
                }
                form {
                    margin-top: 20px;
                }
                label {
                    display: block;
                    margin-bottom: 10px;
                }
                input[type="number"] {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 10px;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <h1>円の面積を求めます!</h1>

            <form action="/present" method="post">
                <label for="radius">半径を入力してください</label>
                <input type="number" id="radius" name="radius" step="0.01"><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/indexOmikuji")
def indexOmikuji():
    html_content = """
    <html>
        <head>
            <title>omikuji</title>
                        <style>
                body {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                }
                h1 {
                    color: #333;
                }
                p {
                    margin-top: 20px;
                }
                a {
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #FF0000;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                }
                a:hover {
                    background-color: #CC0000;
                }
            </style>
        </head>
        <body>
            <h1>今日の運勢</h1>
            <p><a href="/omikuji">おみくじを引く</a></p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
