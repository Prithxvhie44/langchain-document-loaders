from langchain_community.document_loaders.text_loader import TextLoader

loader=TextLoader("cricket.txt", encoding="utf-8")

documents=loader.load()

print(documents)