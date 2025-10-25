# RFP Structured Data Extractor

## Overview
This project extracts structured information from RFP (Request for Proposals) documents in various formats (PDF, HTML) using Large Language Models and presents the results through an interactive Streamlit web application.

## 🌐 Live Demo
**Try the application online:** [https://nagendrakp02-rfp-app-j7lhb0.streamlit.app/](https://nagendrakp02-rfp-app-j7lhb0.streamlit.app/)

## 📂 Sample Output
View example extracted data: [Sample Output Files](https://github.com/nagendrakp02/RFP/tree/main/output)

## Project Structure
```
RFP/
├── src/
│   ├── graphs/
│   │   ├── __init__.py
│   │   └── graph_builder.py      # LangGraph workflow builder
│   ├── llms/
│   │   ├── __init__.py
│   │   └── groqllm.py           # Groq LLM integration
│   ├── nodes/
│   │   ├── __init__.py
│   │   └── rfp_node.py          # Graph nodes for text extraction and structuring
│   ├── parsers/
│   │   ├── html_parser.py       # HTML document parser
│   │   └── pdf_parser.py        # PDF document parser
│   └── states/
│       ├── __init__.py
│       └── rfpstate.py          # State definitions for the workflow
├── output/                       # Sample extracted JSON outputs
├── __init__.py
├── rfputils.py                   # Utility functions and field definitions
├── venv/                         # Virtual environment (auto-generated)
├── .gitignore
├── app.py                        # Main Streamlit application
├── main.py                       # CLI entry point
├── README.md                     # This file
└── requirements.txt              # Project dependencies
```

## Features
- **Multi-format Support**: Processes both PDF and HTML RFP documents
- **LLM-powered Extraction**: Uses Groq LLM models for intelligent data extraction
- **Structured Output**: Extracts 20 predefined fields from RFP documents
- **Interactive Interface**: User-friendly Streamlit web application
- **Multi-file Processing**: Handles multiple documents simultaneously with individual extraction
- **JSON Export**: Exports structured data in JSON format (individual and combined)
- **Graph-based Workflow**: Uses LangGraph for maintainable processing pipelines
- **Cloud Deployment**: Deployed on Streamlit Cloud for easy access

## Requirements
- Python 3.8+
- Groq API Key (free tier available)

## Installation

### 1. Clone or Download the Project
```bash
# Clone the repository
git clone https://github.com/nagendrakp02/RFP.git
cd RFP
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```


## Usage

### Web Interface (Recommended)

#### Option 1: Use the Live Demo
Simply visit [https://nagendrakp02-rfp-app-j7lhb0.streamlit.app/](https://nagendrakp02-rfp-app-j7lhb0.streamlit.app/) and start uploading your RFP documents!

#### Option 2: Run Locally
1. Ensure your virtual environment is activated
2. Run the Streamlit application:
```bash
streamlit run app.py
```
3. Open your browser to `http://localhost:8501`
4. Upload one or multiple RFP documents (PDF/HTML)
5. Click "Extract Structured Data from All Files"
6. View individual extracted JSON data for each file
7. Download results individually or as a combined JSON file


## Extracted Fields
The system extracts the following 20 fields from RFP documents:

| Field | Description |
|-------|-------------|
| Bid Number | Unique identifier for the bid |
| Title | RFP title or subject |
| Due Date | Submission deadline |
| Bid Submission Type | How bids should be submitted |
| Term of Bid | Validity period of the bid |
| Pre Bid Meeting | Pre-bid meeting details |
| Installation | Installation requirements |
| Bid Bond Requirement | Bond requirements |
| Delivery Date | Expected delivery timeline |
| Payment Terms | Payment conditions |
| Any Additional Documentation Required | Extra documentation needed |
| MFG for Registration | Manufacturer registration info |
| Contract or Cooperative to use | Contract details |
| Model_no | Product model number |
| Part_no | Product part number |
| Product | Product description |
| contact_info | Contact information |
| company_name | Company name |
| Bid Summary | Brief summary of the bid |
| Product Specification | Detailed product specifications |

## Technical Implementation

### Architecture
- **LangGraph**: Orchestrates the document processing workflow
- **Groq LLM**: Provides intelligent text understanding and extraction (using llama-3.3-70b-versatile model)
- **Document Parsers**: Handle PDF (pdfplumber) and HTML (BeautifulSoup) parsing
- **Streamlit**: Creates the interactive web interface
- **Streamlit Cloud**: Hosts the deployed application

### Workflow
1. **File Upload**: User uploads one or multiple PDF/HTML documents
2. **Individual Processing**: Each file is processed separately
3. **Text Extraction**: Document-specific parsers extract raw text
4. **LLM Processing**: Groq model analyzes text and extracts structured data
5. **Data Validation**: Ensures all required fields are present
6. **JSON Export**: Formats data for individual or combined download
7. **Results Display**: Shows extraction results for each file with expandable sections

## Dependencies
streamlit
pdfplumber
langchain
langchain_groq
python-dotenv
beautifulsoup4

**Assignment Submission Checklist:**
- ✅ Python script/application that extracts structured data
- ✅ README file with setup and usage instructions
- ✅ JSON output capability for extracted information
- ✅ Support for both PDF and HTML formats
- ✅ LLM integration for intelligent data extraction
- ✅ Clean, documented code structure
- ✅ Live demo deployment on Streamlit Cloud
- ✅ Sample output files in repository


## Author
Developed by Nagendra KP



