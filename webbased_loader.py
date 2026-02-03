from langchain_community.document_loaders import WebBaseLoader

url="https://raw.githubusercontent.com/hwchase17/langchain/main/docs/modules/data_connection/document_loaders/web_based_loader.md"

loader=WebBaseLoader(url)

docs=loader.load()


print(docs[0].page_content)