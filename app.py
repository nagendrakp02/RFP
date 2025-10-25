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

# uploaded_files = st.file_uploader(
#     "Upload RFP PDF or HTML files (multi-select supported)", 
#     type=["pdf", "html", "htm"], 
#     accept_multiple_files=True, 
#     key="rfp_file_uploader_group"
# )

# if uploaded_files:
#     temp_paths = []
#     combined_text = ""
#     for uploaded_file in uploaded_files:
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
#             tmp_file.write(uploaded_file.read())
#             tmp_file_path = tmp_file.name
#             temp_paths.append(tmp_file_path)
#             # Decide parser
#             if tmp_file_path.endswith(".pdf"):
#                 from src.parsers.pdf_parser import extract_text_from_pdf
#                 combined_text += extract_text_from_pdf(tmp_file_path) + "\n"
#             elif tmp_file_path.endswith(".html") or tmp_file_path.endswith(".htm"):
#                 from src.parsers.html_parser import extract_text_from_html
#                 combined_text += extract_text_from_html(tmp_file_path) + "\n"

#     if st.button("Extract Structured Data from All Files"):
#         try:
#             llm = GroqLLM(groq_api_key).get_llm()
#             from src.nodes.rfp_node import RFPNode
#             node = RFPNode(llm)
#             result = node.extract_structured_data({"extracted_text": combined_text})
#             rfp_data = result.get("rfp_data")
#             pretty_json = json.dumps(rfp_data, indent=2) if rfp_data else "{}"
#             st.success("✅ Structured data extracted from all files!")
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
    st.info(f"📁 {len(uploaded_files)} file(s) uploaded")
    
    if st.button("Extract Structured Data from All Files"):
        try:
            # Initialize LLM once
            llm = GroqLLM(groq_api_key).get_llm()
            from src.nodes.rfp_node import RFPNode
            node = RFPNode(llm)
            
            # Store all results
            all_results = []
            
            # Process each file individually
            for idx, uploaded_file in enumerate(uploaded_files, 1):
                st.subheader(f"Processing File {idx}: {uploaded_file.name}")
                
                # Create temporary file for this upload
                with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    tmp_file_path = tmp_file.name
                
                try:
                    # Extract text from this specific file
                    if tmp_file_path.endswith(".pdf"):
                        from src.parsers.pdf_parser import extract_text_from_pdf
                        extracted_text = extract_text_from_pdf(tmp_file_path)
                    elif tmp_file_path.endswith(".html") or tmp_file_path.endswith(".htm"):
                        from src.parsers.html_parser import extract_text_from_html
                        extracted_text = extract_text_from_html(tmp_file_path)
                    else:
                        st.error(f"❌ Unsupported file type: {uploaded_file.name}")
                        continue
                    
                    # Extract structured data for this file
                    with st.spinner(f"Extracting data from {uploaded_file.name}..."):
                        result = node.extract_structured_data({"extracted_text": extracted_text})
                        rfp_data = result.get("rfp_data")
                    
                    # Display results for this file
                    if rfp_data:
                        st.success(f"✅ Data extracted from {uploaded_file.name}")
                        pretty_json = json.dumps(rfp_data, indent=2)
                        
                        # Show JSON in expandable section
                        with st.expander(f"View JSON for {uploaded_file.name}", expanded=True):
                            st.code(pretty_json, language="json")
                        
                        # Add to results collection
                        all_results.append({
                            "filename": uploaded_file.name,
                            "data": rfp_data
                        })
                        
                        # Individual download button
                        st.download_button(
                            f"⬇️ Download JSON for {uploaded_file.name}",
                            pretty_json,
                            file_name=f"rfp_{uploaded_file.name.rsplit('.', 1)[0]}.json",
                            mime="application/json",
                            key=f"download_{idx}"
                        )
                    else:
                        st.warning(f"⚠️ No data extracted from {uploaded_file.name}")
                    
                    # Clean up temp file
                    os.unlink(tmp_file_path)
                    
                    st.divider()
                    
                except Exception as file_error:
                    st.error(f"❌ Error processing {uploaded_file.name}: {file_error}")
                    if os.path.exists(tmp_file_path):
                        os.unlink(tmp_file_path)
            
            # Download all results as one combined JSON
            if all_results:
                st.success(f"🎉 Successfully processed {len(all_results)} file(s)!")
                combined_json = json.dumps(all_results, indent=2)
                st.download_button(
                    "⬇️ Download All Results (Combined JSON)",
                    combined_json,
                    file_name="rfp_all_results.json",
                    mime="application/json",
                    key="download_all"
                )
                
        except Exception as e:
            st.error(f"❌ Error: {e}")


def main():
    print("Hello from RFP extraction!")


if __name__ == "__main__":
    main()
