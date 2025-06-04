#Setting Up the Project
First, let’s create a new directory for our project and set up the required dependencies:

```bash
mkdir mcp-sentiment
cd mcp-sentiment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install "gradio[mcp]" textblob
```

