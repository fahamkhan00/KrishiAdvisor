from langchain.chains import RetrievalQA
from pipeline.retriever import build_or_load_vectorstore
from pipeline.fallback import fallback_answer
from models.llm_loader import load_llm
from langchain_community.llms import HuggingFacePipeline

def create_rag_chain():
    llm_pipe = load_llm()
    vectorstore = build_or_load_vectorstore()

    rag = RetrievalQA.from_chain_type(
        llm=HuggingFacePipeline(pipeline=llm_pipe),
        retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
        return_source_documents=True
    )

    return rag, llm_pipe
