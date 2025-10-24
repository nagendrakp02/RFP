# import streamlit as st
# from src.graphs.graph_builder import GraphBuilder
# from src.llms.groqllm import GroqLLM
# from dotenv import load_dotenv
# import os
# import tempfile
# import json

# # Load environment variables
# load_dotenv()
# groq_api_key = os.getenv("GROQ_API_KEY")

# st.set_page_config(page_title="RFP Structured Data Extractor", layout="centered")
# st.title("📄 RFP Structured Data Extractor")

# uploaded_file = st.file_uploader(
#     "Upload RFP PDF or HTML file", type=["pdf", "html", "htm"], key="rfp_file_uploader"
# )

# if uploaded_file:
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
#         tmp_file.write(uploaded_file.read())
#         tmp_file_path = tmp_file.name

#     if st.button("Extract Structured Data"):
#         try:
#             llm = GroqLLM(groq_api_key).get_llm()
#             graph_builder = GraphBuilder(llm)
#             graph = graph_builder.setup_graph()
#             state = graph.invoke({"file_path": tmp_file_path})
#             rfp_data = state.get("rfp_data")
#             pretty_json = json.dumps(rfp_data, indent=2) if rfp_data else "{}"
#             st.success("✅ Structured data extracted!")
#             st.code(pretty_json, language="json")
#             st.download_button(
#                 "Download JSON",
#                 pretty_json,
#                 file_name="rfp_structured_data.json",
#                 mime="application/json"
#             )
#         except Exception as e:
#             st.error(f"❌ Error: {e}")


import streamlit as st
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM
from dotenv import load_dotenv
import os
import tempfile
import json

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="RFP Structured Data Extractor", layout="centered")
st.title("📄 RFP Structured Data Extractor")

uploaded_files = st.file_uploader(
    "Upload RFP PDF or HTML files (multi-select supported)", 
    type=["pdf", "html", "htm"], 
    accept_multiple_files=True, 
    key="rfp_file_uploader_group"
)

if uploaded_files:
    temp_paths = []
    combined_text = ""
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name
            temp_paths.append(tmp_file_path)
            # Decide parser
            if tmp_file_path.endswith(".pdf"):
                from src.parsers.pdf_parser import extract_text_from_pdf
                combined_text += extract_text_from_pdf(tmp_file_path) + "\n"
            elif tmp_file_path.endswith(".html") or tmp_file_path.endswith(".htm"):
                from src.parsers.html_parser import extract_text_from_html
                combined_text += extract_text_from_html(tmp_file_path) + "\n"

    if st.button("Extract Structured Data from All Files"):
        try:
            llm = GroqLLM(groq_api_key).get_llm()
            from src.nodes.rfp_node import RFPNode
            node = RFPNode(llm)
            result = node.extract_structured_data({"extracted_text": combined_text})
            rfp_data = result.get("rfp_data")
            pretty_json = json.dumps(rfp_data, indent=2) if rfp_data else "{}"
            st.success("✅ Structured data extracted from all files!")
            st.code(pretty_json, language="json")
            st.download_button(
                "Download JSON",
                pretty_json,
                file_name="rfp_structured_data.json",
                mime="application/json"
            )
        except Exception as e:
            st.error(f"❌ Error: {e}")
