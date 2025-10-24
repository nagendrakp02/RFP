from bs4 import BeautifulSoup

def extract_text_from_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    return soup.get_text(separator="\n")
