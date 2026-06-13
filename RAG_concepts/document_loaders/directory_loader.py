# directory loader helps us load multiple files at once

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob='*.pdf',
    loader_cls= PyPDFLoader
)

docs =  loader.lazy_load()

for i in docs:
    print(i.metadata)