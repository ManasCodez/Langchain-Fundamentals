from langchain_text_splitters import RecursiveCharacterTextSplitter


text= 'Artificial intelligence is transforming the way people work, learn, and communicate. From virtual assistants that answer questions to recommendation systems that suggest movies and products, AI has become a part of everyday life. Businesses use machine learning to analyze customer behavior, detect fraud, and automate repetitive tasks, allowing employees to focus on more creative and strategic work. In education, AI-powered tools provide personalized learning experiences by adapting lessons to individual students and identifying areas where they need additional support. Healthcare professionals use AI to assist in diagnosing diseases, analyzing medical images, and predicting patient outcomes, improving both speed and accuracy. Despite these advantages, responsible development remains essential. Developers and organizations must address concerns related to privacy, bias, transparency, and security to ensure that AI systems are fair and trustworthy. Governments and researchers are also creating guidelines and regulations to encourage ethical innovation while protecting users. As technology continues to evolve, collaboration between engineers, policymakers, educators, and the public will play a crucial role in shaping its future. By combining human creativity with intelligent algorithms, society can solve complex problems, increase productivity, and create opportunities that were previously unimaginable for people around the world.'

splitter = RecursiveCharacterTextSplitter( 
            chunk_size = 100,
            chunk_overlap = 0
)


# splits in this order=> paragraph - sentence - word - character
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)

