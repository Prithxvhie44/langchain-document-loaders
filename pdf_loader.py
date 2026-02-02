from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

loader=PyPDFLoader("dl-curriculum.pdf")

docs=loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)