from src.rfputils import assignment_fields, empty_assignment_json

class RFPNode:
    def __init__(self, llm):
        self.llm = llm

    def extract_text(self, state):
        file_path = state["file_path"]
        if file_path.endswith(".pdf"):
            from src.parsers.pdf_parser import extract_text_from_pdf
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith(".html") or file_path.endswith(".htm"):
            from src.parsers.html_parser import extract_text_from_html
            text = extract_text_from_html(file_path)
        else:
            raise ValueError("Unsupported file type")
        return {"extracted_text": text}

    def extract_structured_data(self, state):
        fields = assignment_fields()
        field_prompt = ", ".join([f'"{f}"' for f in fields])
        prompt = (
            "Carefully extract ONLY the following fields as a JSON object with EXACT field names (including capitalization and spaces):\n"
            + field_prompt +
            "\nIf a field is not present in the document, set it to an empty string. Do not generate extra fields.\n"
            "Example output:\n"
            + "{\n" +
              ",\n".join([f'  "{f}": ""' for f in fields]) +
              "\n}\n" +
            f"\nRFP TEXT:\n{state['extracted_text'][:8000]}\n\nRespond only with valid JSON."
        )
        response = self.llm.invoke(prompt)
        import json
        try:
            # Find first and last curly to robustly parse large outputs
            txt = response.content
            start = txt.find("{")
            end = txt.rfind("}")
            json_str = txt[start:end+1]
            data = json.loads(json_str)
            # Ensure missing fields are added as empty strings
            for f in fields:
                if f not in data:
                    data[f] = ""
            # Remove extra fields if present
            for k in list(data):
                if k not in fields:
                    del data[k]
            return {"rfp_data": data}
        except Exception:
            return {"rfp_data": empty_assignment_json()}
