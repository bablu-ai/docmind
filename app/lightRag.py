# app/agents.py
# Initialize LightRAG
import asyncio
import sys

from langchain_core.documents import Document

from ingestion_vector import DocumentProcessor
import numpy as np

from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from flask import Flask, request, jsonify
from flask_cors import CORS

import os

from flask import Flask, request, jsonify
# from phoenix.otel import register
# from openinference.instrumentation.langchain import LangChainInstrumentor

from lightrag import LightRAG, QueryParam

from lightrag.utils import EmbeddingFunc, setup_logger


from app.ai_models import AVAILABLE_EMBEDDINGS, AVAILABLE_LLMS
from app.config import DATA_DIR, OPENAI_API_KEY

# tracer_provider = register(project_name="DocMind",batch=True, auto_instrument=True, endpoint="http://localhost:4317")
#
# lanfchainInstrumentor = LangChainInstrumentor()
# lanfchainInstrumentor.instrument( tracer_provider=tracer_provider)

setup_logger(logger_name="docMind", level="DEBUG", enable_file_logging=True, log_file_path=".\docMind.log")


async def embedding_func(text: list[str]) ->np.ndarray:
    return await openai_embed(text,
    model=AVAILABLE_EMBEDDINGS["openai-small"]["model"],
    base_url="https://api.openai.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"));

async def llm_model_func(prompt:str, system_prompt=None,
                         history_messages=[], keywords_extraction=False, **kwargs) ->str:
    return await openai_complete_if_cache(
                    prompt,
                    model=AVAILABLE_LLMS["gpt-4o"]["model"],
                    system_prompt=system_prompt,
                    history_messages=history_messages,
                    base_url =  "https://api.openai.com/v1",
                    api_key = os.getenv("OPENAI_API_KEY"),
                    **kwargs);


async def wait():
    try:
        await asyncio.sleep(asyncio.sleep(7), timeout=1)
    except asyncio.TimeoutError:
        print("timeout errors")
        sys.exit(1)
    return


async def initialize_lightRag():
    lightRag=LightRAG(
        working_dir=DATA_DIR,
        llm_model_func=llm_model_func,
        embedding_func=EmbeddingFunc(
            embedding_dim=8192,
            max_token_size=8192,
            func=embedding_func),
        llm_model_name=AVAILABLE_LLMS["gpt-4o"]["model"],
    )
    await lightRag.initialize_storages()
    await initialize_pipeline_status()
    return lightRag;


dp = DocumentProcessor(DATA_DIR);
all_chunk_documents: list[Document] = dp.ingest_all()

loop = asyncio.get_event_loop()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/")
def notify():
    global rag
    if rag:
        return "Initialized RAG"
    else:
        return "RAG Initializing"

@app.route('/agent')
def call_agent():
    global rag
    query_text = request.args.get('query')
    if query_text is None:
        return "No query provided"
    os.environ["SSL_CERT_FILE"] = "./wf-cabundle.crt"
    # Initialize RAG instance
    return rag.query(
        query_text,
        param=QueryParam(mode="global", response_type="Bullet Points", only_need_context=False,max_token_for_local_context=2048, max_token_for_global_context=8192)
    )


@app.route('/insert')
def insert():
    global rag
    documents = dp.ingest_all()
    for document in documents:
        rag.insert(document.page_content)
    return "Text inserted"

if __name__ == "__main__":
    print("Starting LightRag App")
    rag = loop.run_until_complete(initialize_lightRag())
    print("Initialized LightRag")
    app.run(port=5001, debug=True, use_reloader=False)

