###################################################################
# Aim:
# 1. Integrate code with an LLM API (eg OpenAI, anthropic or local Olama)
# 2. Use LLM to search PDF - solution: vector store! 
# 3. Use word embedding, FAISS and qa_chain
###################################################################

###################################################################
# Load packages
###################################################################
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains.question_answering import load_qa_chain

###################################################################
# Declare parameters
###################################################################

###################################################################
# Set up streamlit framework
###################################################################
st.title('Langchain Demo Llama2 - Chat with your PDF')
user_file = st.file_uploader('Hey there, curious explorer! Upload your PDF', type = 'pdf')

def main(user_file):


    ###################################################################
    # 1. Load file and ask a question
    ###################################################################
    if user_file is not None:
        pdf_reader = PdfReader(user_file)
        raw_text = ""
        for page in pdf_reader.pages:
            raw_text+=page.extract_text()

    user_query = st.text_input('Ask a question.')
        
    ###################################################################
    # 2. Split text to maintain prompt window or tokens limit.
    ###################################################################
    text_splitter = CharacterTextSplitter(separator = "\n", chunk_size = 2048, chunk_overlap = 100, length_function = len)
    chunks = text_splitter.split_text(raw_text)

    ###################################################################
    # 3. Save texts in a vector database
    ###################################################################
    # create word embeddings
    embedding = OllamaEmbeddings(model = 'llama2')
    knowledgeBase = FAISS.from_texts(texts = chunks, embedding = embedding)

    ###################################################################
    # 4. Set up LLM with Ollama and LLM chain
    ###################################################################
    llm = Ollama(model = 'llama2')
    chain = load_qa_chain(llm = llm, chain_type = "stuff")

    ###################################################################
    # 5. Run LLM chain
    ###################################################################
    if len(user_query)>0:

        # find the questions
        docs = knowledgeBase.similarity_search(user_query)
        # provide chain with docs and question
        st.write(chain({'input_documents':docs, 'question':user_query}))

###################################################################
# Driver
###################################################################
if __name__ == '__main__':

    if (user_file is not None) and (user_file.name.lower().endswith('.pdf')):
        main(user_file = user_file)


