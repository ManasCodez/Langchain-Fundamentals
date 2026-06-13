from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

code = """class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def display(self, result):
        print("Result:", result)


calc = Calculator()

sum_result = calc.add(10, 20)
calc.display(sum_result)

product_result = calc.multiply(5, 6)
calc.display(product_result)"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 200,
    chunk_overlap = 20
)

res = splitter.split_text(code)
print(len(res))
print(res[0])
print()
print(res[1])