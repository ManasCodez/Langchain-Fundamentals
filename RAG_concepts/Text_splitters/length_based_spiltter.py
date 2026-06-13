from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader('Resume.pdf')
text = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10,
    separator=''
)

result = splitter.split_documents(text)
print(result[0].page_content)
print()
print(result[1].page_content)
