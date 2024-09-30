import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import OllamaEmbeddings
#from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_groq import ChatGroq

def prepare_prompt(user_prompt):
    pre_prompt = """You are Cruise, an AI assistant. When responding to questions:

    1. Identify yourself as Cruise, but do so briefly and only when necessary.
    2. Provide direct, concise answers without unnecessary friendliness or small talk.
    3. Do not use phrases like "according to the context" or "as an AI model" or any related things like this.
    4. Avoid overly formal or robotic language. Respond as a knowledgeable human would.
    5. Don't apologize or express uncertainty. If you don't have enough information, say so directly.
    6. Use contractions and natural speech patterns, but maintain a professional tone.
    7. If the question relates to you (Cruise), answer accordingly, but keep the focus on providing useful information.

    Now, address the following question or request:
    """
    return f"{pre_prompt}\n\n{user_prompt}"

def ragLlama(prompt):
    try:
        # Load PDF documents from the specified directory
        loader = PyPDFDirectoryLoader("RAG/data")
        the_text = loader.load()
        
        # Split the loaded text into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(the_text)

        # Create or load the vector store
        persist_directory = "RAG"
        if not os.path.exists(persist_directory):
            vectorstore = Chroma.from_documents(
                documents=docs,
                collection_name="ollama_embeds",
                embedding=OllamaEmbeddings(model='nomic-embed-text'),
                persist_directory=persist_directory
            )
            vectorstore.persist()
        else:
            vectorstore = Chroma(
                persist_directory=persist_directory,
                embedding_function=OllamaEmbeddings(model='nomic-embed-text'),
                collection_name="ollama_embeds"
            )

        retriever = vectorstore.as_retriever()
        
        llm = ChatGroq(
            groq_api_key="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",
            model_name='llava-v1.5-7b-4096-preview'
        )
        
        rag_template = """
            Cruise here. I'll answer your question based on the following information:
            {context}
            Question: {question}
            Answer:
        """
        
        rag_prompt = ChatPromptTemplate.from_template(rag_template)
        
        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | rag_prompt
            | llm
            | StrOutputParser()
        )

        full_prompt = prepare_prompt(prompt)
        response = rag_chain.invoke(full_prompt)
        return response.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}. Please try again or contact support if the issue persists."

# Run the function
if __name__ == "__main__":
    result = ragLlama("What is Aditya's experience?")
    print(result)