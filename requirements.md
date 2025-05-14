Requirements: https://docs.google.com/document/d/1PmoDBxf_VFEzNpUg0VtuKbCysQSqzxcqDWLgne7TSE8/edit?usp=sharing


My understanding of your goal is to create a sophisticated chatbot system with the following key characteristics:

* **Agentic Core:** A central "master agent" (likely built with LangChain/LangGraph) that understands complex user queries, potentially breaking them down, deciding which specialized tool(s) to use, and managing the conversation flow.
* **Tool-Based Architecture:** The agent delegates tasks to specific tools:
    * Stock Info (Yahoo Finance)
    * Account API (Local endpoint)
    * Enhanced Search (LLM-powered query optimization + context)
    * Document Processing (LightRAG primary, LangChain fallback for PDF, DOCX, TXT)
    * Response Refinement (Tone, summarization, consistency)
* **RAG Integration:** Heavy reliance on LightRAG for Retrieval Augmented Generation, including graph-based search and dynamic mode selection (mix, global, local, naive). It will also handle vector store integration and reranking.
* **Context Management:** Robust conversation history tracking (ConversationBufferMemory) and persistence, likely linked to user accounts stored in MongoDB.
* **User Management:** MongoDB stores user details and conversation history (userId, conversationId, query/response pairs).
* **Technology Stack:** Python is central, leveraging LightRAG, LangChain/LangGraph, LiteLLM (for model abstraction), potentially LlamaIndex (if needed), and MongoDB.
* **Phased Development:** You want to build this incrementally, visualizing each phase with a detailed Mermaid diagram.
* **Observability:** Integration with Phoenix/OpenTelemetry for tracing.
* **UI:** A React-based frontend for user interaction, chat history management, LLM selection, and preferences.
* **Deployment:** Consideration for deployment on GCP, Azure, or AWS.

**2. List of Things To Be Done (Based on your request):**

1.  **Phase a Diagram:** Basic UI + Backend (Query -> LLM -> Response).
2.  **Phase b Diagram:** Add LangChain Agent + Stock Tool.
3.  **Phase c Diagram:** Add Weather Tool + Agent routing logic (2 tools).
4.  **Phase d Diagram:** Add Vector DB Search Tool + Agent routing logic (3 tools).
5.  **Phase e Diagram:** Integrate RAG results into context refinement.
6.  **Phase f Diagram:** Implement multi-tool chaining/sequencing based on query analysis.
7.  **Phase g Diagram:** Add Final Response Refiner Tool.
8.  **Phase h Diagram:** Design React UI components and interactions.
9.  **Phase i Diagram:** Design Backend APIs (DB interaction, external APIs).
10. **Phase j Diagram:** Integrate Phoenix/OpenTelemetry tracing.
11. **Phase k Diagram:** Add LightRAG Document Processing (Upload).
12. **Phase l Diagram:** Add LightRAG Document Processing (Web Scraping).
13. **High-Level System Architecture Diagram.**
14. **Data Flow Diagram (DFD).**
15. **Component Level Architecture Diagram.**
16. **RAG/LLM-specific Architecture Diagram.**
17. **Security Architecture Diagram.**
18. **Infrastructure Diagram (GCP).**
19. **Infrastructure Diagram (Azure).**
20. **Infrastructure Diagram (AWS).**
21. **Python Code Implementation** (Future Step).

**Next Step:**

1. See PHASE-1.md, and PHASE-1.mermaid
1. See PHASE-2.md, and PHASE-2.mermaid
1. See PHASE-3.md, and PHASE-3.mermaid
1. See PHASE-4.md, and PHASE-4.mermaid
1. See PHASE-5.md, and PHASE-5.mermaid