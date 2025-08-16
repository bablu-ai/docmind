from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

app = FastAPI(title=“PDF Download Server”)

# Directory where your PDFs are stored

PDF_DIR = “pdfs”

# Create the PDF directory if it doesn’t exist

Path(PDF_DIR).mkdir(exist_ok=True)

# Dictionary of your PDFs (filename -> display name)

PDF_FILES = {
“document1.pdf”: “User Manual”,
“document2.pdf”: “Quick Start Guide”,
“document3.pdf”: “Technical Specifications”,
“document4.pdf”: “Installation Guide”
}

@app.get(”/”, response_class=HTMLResponse)
async def home():
“”“Main page with download links”””
html_content = “””
<!DOCTYPE html>
<html>
<head>
<title>PDF Downloads</title>
<style>
body {
font-family: Arial, sans-serif;
max-width: 800px;
margin: 50px auto;
padding: 20px;
background-color: #f5f5f5;
}
.container {
background-color: white;
padding: 30px;
border-radius: 10px;
box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
h1 {
color: #333;
text-align: center;
margin-bottom: 30px;
}
.pdf-link {
display: block;
padding: 15px 20px;
margin: 10px 0;
background-color: #007bff;
color: white;
text-decoration: none;
border-radius: 5px;
transition: background-color 0.3s;
}
.pdf-link:hover {
background-color: #0056b3;
}
.pdf-icon {
margin-right: 10px;
}
</style>
</head>
<body>
<div class="container">
<h1>📁 PDF Downloads</h1>
<div class="links">
“””

```
# Add download links for each PDF
for filename, display_name in PDF_FILES.items():
    html_content += f'''
            <a href="/download/{filename}" class="pdf-link">
                <span class="pdf-icon">📄</span>
                {display_name}
            </a>
    '''

html_content += """
        </div>
    </div>
</body>
</html>
"""

return html_content
```

@app.get(”/download/{filename}”)
async def download_pdf(filename: str):
“”“Download a specific PDF file”””
# Check if the filename is in our allowed list
if filename not in PDF_FILES:
raise HTTPException(status_code=404, detail=“PDF not found”)

```
file_path = os.path.join(PDF_DIR, filename)

# Check if file exists
if not os.path.exists(file_path):
    raise HTTPException(status_code=404, detail="File not found on server")

return FileResponse(
    path=file_path,
    filename=filename,
    media_type='application/pdf'
)
```

@app.get(”/list”)
async def list_pdfs():
“”“API endpoint to get list of available PDFs”””
return {“pdfs”: PDF_FILES}

if **name** == “**main**”:
import uvicorn
uvicorn.run(app, host=“0.0.0.0”, port=8000)
