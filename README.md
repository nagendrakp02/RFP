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
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
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

**To get a Groq API key:**
1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

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

### Command Line Interface
```bash
python main.py
```

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
```
streamlit>=1.28.0
langchain-groq==0.1.9
langchain-core==0.2.0
langgraph==0.1.0
pdfplumber>=0.7.0
beautifulsoup4>=4.12.0
python-dotenv>=1.0.0
pydantic>=2.0.0
lxml>=4.9.0
```

## Troubleshooting

### Common Issues

**1. Module Import Errors**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Reinstall dependencies with correct versions
pip install langchain-core==0.2.0 langchain-groq==0.1.9 langgraph==0.1.0
```

**2. Groq API Key Issues**
- Verify your `.env` file contains the correct API key
- Check that the key is active at [console.groq.com](https://console.groq.com/)
- Ensure no extra spaces or quotes around the key
- For Streamlit Cloud deployment, add the key in Secrets management

**3. File Upload Issues**
- Supported formats: PDF, HTML, HTM
- Check file permissions and size limits
- Ensure files are not corrupted

**4. Streamlit Not Starting**
```bash
# Try specifying port explicitly
streamlit run app.py --server.port 8501
```

**5. Dependency Version Conflicts**
```bash
# Uninstall conflicting packages
pip uninstall langchain-groq langchain-core langgraph -y

# Install specific compatible versions
pip install langchain-core==0.2.0 langchain-groq==0.1.9 langgraph==0.1.0
```

## Output Format
The extracted data is returned in JSON format:

### Individual File Output
```json
{
  "Bid Number": "RFP-2024-001",
  "Title": "Software Development Services",
  "Due Date": "2024-12-31",
  "Bid Submission Type": "Electronic",
  "Term of Bid": "30 days",
  "Pre Bid Meeting": "2024-11-15 at 10:00 AM",
  "Installation": "On-site installation required",
  "Bid Bond Requirement": "5% of bid amount",
  // ... other 12 fields
}
```

### Combined Output (Multiple Files)
```json
[
  {
    "filename": "rfp_document1.pdf",
    "data": {
      "Bid Number": "RFP-2024-001",
      "Title": "Software Development Services",
      // ... all 20 fields
    }
  },
  {
    "filename": "rfp_document2.html",
    "data": {
      "Bid Number": "RFP-2024-002",
      "Title": "Hardware Procurement",
      // ... all 20 fields
    }
  }
]
```

## Performance Notes
- Processing time depends on document size and complexity
- Each file is processed individually for accurate extraction
- Groq free tier has rate limits; consider upgrading for high-volume usage
- Large documents are automatically truncated to 8000 characters for LLM processing
- Multi-file processing shows progress for each file separately

## Repository
- **GitHub Repository**: [https://github.com/nagendrakp02/RFP](https://github.com/nagendrakp02/RFP)
- **Sample Outputs**: [https://github.com/nagendrakp02/RFP/tree/main/output](https://github.com/nagendrakp02/RFP/tree/main/output)

## Contributing
1. Fork the repository
2. Follow the existing code structure
3. Add proper error handling
4. Include docstrings for new functions
5. Test with various RFP document formats
6. Submit a pull request

## License
This project is developed for educational and assignment purposes.

## Support
For technical issues:
1. Check the troubleshooting section above
2. Verify all dependencies are correctly installed with compatible versions
3. Ensure your Groq API key is valid and properly configured
4. Review the console output for specific error messages
5. Check sample outputs at [https://github.com/nagendrakp02/RFP/tree/main/output](https://github.com/nagendrakp02/RFP/tree/main/output)

## Author
Developed by Nagendra KP

---

## Quick Start Guide

1. **Try it online**: Visit [https://nagendrakp02-rfp-app-j7lhb0.streamlit.app/](https://nagendrakp02-rfp-app-j7lhb0.streamlit.app/)
2. **Upload your RFP documents** (PDF or HTML)
3. **Click Extract** to process all files
4. **View and download** the structured JSON data
5. **Check sample outputs** at [output folder](https://github.com/nagendrakp02/RFP/tree/main/output)

---

**Assignment Submission Checklist:**
- ✅ Python script/application that extracts structured data
- ✅ README file with setup and usage instructions
- ✅ JSON output capability for extracted information
- ✅ Support for both PDF and HTML formats
- ✅ LLM integration for intelligent data extraction
- ✅ Clean, documented code structure
- ✅ Live demo deployment on Streamlit Cloud
- ✅ Sample output files in repository