from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext, StorageContext
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
    loader = PyPDFDirectoryLoader("RAG/data")
    the_text = loader.load()
    
    # Split the loaded text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(the_text)

    # Initialize the vector store with embeddings
    try:
        vectorstore = Chroma.from_documents(
            documents=docs,
            collection_name="ollama_embeds",
            embedding=OllamaEmbeddings(model='nomic-embed-text'),  # Ensure this model is available
        )
    except ValueError as e:
        print(f"Error initializing vector store: {e}")
        return

    # Create a retriever from the vector store
    retriever = vectorstore.as_retriever()

    # Initialize the chat model with your API key and model name
    from langchain_groq import ChatGroq
    llm = ChatGroq(
        groq_api_key="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",
        model_name='llava-v1.5-7b-4096-preview'
    )
    
    # Define the RAG prompt template
    rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    
    rag_prompt = ChatPromptTemplate.from_template(rag_template)
    
    # Create the RAG chain for processing input and generating output
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | rag_prompt
        | llm
        | StrOutputParser()
    )

    # Invoke the chain with a sample question
    try:
        response = rag_chain.invoke(str(prompt))
        print(response)
        return response
    except Exception as e:
        print(f"Error during invocation: {e}")

# Run the function
if __name__ == "__main__":
    ragLlama("What is in the document?")