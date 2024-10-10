import re
from typing import Union
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from openai import OpenAI

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application with OpenAI integration.",
    version="1.0.0"
)

client = OpenAI(api_key="sk-PfGMnvZDBT6eIXLfTi182TqIhqjwCLbnLO7wxANicRT3BlbkFJONEyDnXG0oatTe3-ZgqRMSBBc917_5aAxXzWlm09oA")



@app.get("/", include_in_schema=False)
async def redoc():
    return get_redoc_html(openapi_url="/openapi.json", title="ReDoc - Auth Service")


# Swagger docs at /docs
@app.get("/docs", include_in_schema=False)
async def swagger_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Swagger - Auth Service")


@app.get("/chat_gpt/")
def read_item(sentence: Union[str, None] = None):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "Vous êtes un assistant utile. Vous devez répondre à la question de manière courte et concise sur la maladie de Parkinson."},
            {"role": "user", "content": sentence}
        ]
    )

    # Return the generated response
    return completion.choices[0].message
