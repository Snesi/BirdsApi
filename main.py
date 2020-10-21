import uvicorn
import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates("templates")

@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request
    })


@app.get("/birds")
def get_birds(request: Request):
    url = "https://api.ebird.org/v2/data/obs/US-NC/recent"

    payload = {}
    headers = {
        'X-eBirdApiToken': '64noeoqem1je'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

