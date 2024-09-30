#from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext, StorageContext
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def ragLlama(prompt):
    # Load PDF documents from the specified directory
    loader = PyPDFDirectoryLoader("RAG\data")
    the_text = loader.load()
    
    # Split the loaded text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(the_text)
    print("\n\n\n", docs, "\n\n\n")


    try:
        vectorstore = Chroma.from_documents(
            documents=docs,
            collection_name="ollama_embeds",
            embedding=OllamaEmbeddings(model='nomic-embed-text'),
            persist_directory="RAG"
        )

        print(type(vectorstore))
    except ValueError as e:
        print(f"Error initializing vector store: {e}")
        return
    
    try:
        vectorstore = Chroma(
            persist_directory="RAG",
            embedding_function=OllamaEmbeddings(model='nomic-embed-text'),
            collection_name="ollama_embeds"
        )

        print(type(vectorstore))
    except ValueError as e:
        print(f"Error Getting vector store: {e}")
        return

    retriever = vectorstore.as_retriever()
    
    from langchain_groq import ChatGroq
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

    pre_prompt = """You are Cruise, an AI assistant. When responding to questions:

        1. Identify yourself as Cruise, but do so briefly and only when necessary.
        2. Provide direct, concise answers without unnecessary friendliness or small talk.
        3. Do not use phrases like "according to the context" or "as an AI model" or any related things like this..
        4. Avoid overly formal or robotic language. Respond as a knowledgeable human would.
        5. Don't apologize or express uncertainty. If you don't have enough information, say so directly.
        6. Use contractions and natural speech patterns, but maintain a professional tone.
        7. If the question relates to you (Cruise), answer accordingly, but keep the focus on providing useful information.
        Now, address the following question or request:
    """
    
    rag_prompt = ChatPromptTemplate.from_template(rag_template)
    
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | rag_prompt
        | llm
        | StrOutputParser()
    )

    try:
        response = rag_chain.invoke(str(prompt))
        print(response)
        return response
    except Exception as e:
        print(f"Error during invocation: {e}")

        

# Run the function
if __name__ == "__main__":
    ragLlama("What is aditya's experience?")
