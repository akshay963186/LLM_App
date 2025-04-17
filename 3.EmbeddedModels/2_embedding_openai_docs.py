from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimension=32)
docoments=[
    "this is boy",
    "this is cat",
    "this is girl"
]
result=embedding.embed_documents(docoments)
print(str(result))