
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, CSVLoader


loader = CSVLoader(
    file_path = 'Salary_Data[1].csv'
)

data = loader.lazy_load()

for i in data:
    print(i.page_content)
