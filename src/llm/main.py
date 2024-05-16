from credentials import OPENAI_API_KEY

from .vector.main import vectorstore
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

class ChatBot:

    def __init__(self):

        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)
        self.vectorstore = vectorstore
        self.retriever = vectorstore.as_retriever()

    def ask(self, question: str):

        template = '''
        You are a helpful assistant that answers questions about World War 2.
        You will be given context for the questions, and answer the user based on the context and whatever knowledge you might already have. 
        If the user asks any questions outside the scope of World War 2 or the context, you will simply state that you do not know the answer.
        
        Context: 
        {context}

        Question: 
        {input}

        Answer:
        '''

        prompt = PromptTemplate(
            template=template,
            input_variables=['context', 'input']
        )

        document_chain = create_stuff_documents_chain(self.llm, prompt)
        retrieval_chain = create_retrieval_chain(self.retriever, document_chain)

        response = retrieval_chain.invoke({'input': question})

        self.question = question
        self.answer = 

        return retrieval_chain.invoke({
            'input': question
        })

         


