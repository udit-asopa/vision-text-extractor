# Document Processing Tutorial

Master document processing with Vision Text Extractor! This comprehensive tutorial covers business documents, forms, contracts, and more.

## 📋 **What You'll Learn**

- Process various business document types
- Extract structured data with custom prompts
- Handle different file formats and quality levels
- Automate document workflows
- Compare accuracy across different providers

## 🏢 **Business Document Types**

### **📄 Invoices & Bills**

#### Basic Invoice Processing
```bash
# Extract key invoice information
python main.py invoice.pdf \
  --prompt "Extract: invoice number, date, vendor, total amount, due date"

# Structured JSON output
python main.py invoice.jpg \
  --prompt "Extract invoice data as JSON with fields: invoice_id, date, vendor_name, line_items, subtotal, tax, total"
```

#### Batch Invoice Processing
```bash
# Process multiple invoices
for invoice in invoices/*.pdf; do
  echo "Processing: $invoice"
  python main.py "$invoice" \
    --prompt "Extract: invoice number, date, vendor, total" \
    > "processed/$(basename "$invoice" .pdf).txt"
done
```

**Expected Output:**
```
Invoice Number: INV-2024-001
Date: March 15, 2024
Vendor: ABC Supply Company
Total Amount: $1,247.50
Due Date: April 15, 2024
```

---

### **🏦 Financial Documents**

#### Bank Statements
```bash
# Extract all transactions
python main.py bank-statement.pdf \
  --prompt "Extract all transactions with: date, description, amount, balance"

# Focus on specific transaction types
python main.py statement.pdf \
  --prompt "Extract only deposits and their amounts with dates"
```

#### Credit Card Statements
```bash
# Get spending summary
python main.py cc-statement.pdf \
  --prompt "Extract: statement period, previous balance, payments, new charges, current balance, minimum payment"

# Transaction details
python main.py cc-statement.pdf \
  --prompt "List all transactions with date, merchant, amount, and category"
```

---

### **📋 Forms & Applications**

#### Insurance Forms
```bash
# Extract form data
python main.py insurance-form.pdf \
  --prompt "Extract all filled form fields and their values, including: name, policy number, claim details, date of incident"

# Medical claim forms
python main.py medical-claim.pdf \
  --prompt "Extract: patient info, provider details, diagnosis codes, procedure codes, amounts"
```

#### Job Applications
```bash
# Extract applicant information
python main.py job-application.pdf \
  --prompt "Extract: applicant name, contact info, work experience, education, skills"

# Government forms
python main.py tax-form.pdf \
  --prompt "Extract all numerical values and their corresponding field labels"
```

---

### **📑 Contracts & Legal Documents**

#### Contract Analysis
```bash
# Extract key contract terms
python main.py contract.pdf \
  --prompt "Extract: parties involved, effective date, termination date, key obligations, payment terms"

# Lease agreements
python main.py lease.pdf \
  --prompt "Extract: property address, lease term, monthly rent, security deposit, special conditions"
```

#### Legal Document Review
```bash
# Identify important clauses
python main.py legal-doc.pdf \
  --prompt "Identify and extract: liability clauses, termination conditions, dispute resolution procedures"
```

## 🎯 **Advanced Extraction Techniques**

### **Structured Data Extraction**

#### Table Processing
```bash
# Extract tables as structured data
python main.py financial-report.pdf \
  --prompt "Extract the financial table preserving rows and columns. Format as: Item | Q1 | Q2 | Q3 | Q4"

# Price lists
python main.py price-list.jpg \
  --prompt "Extract pricing table with: Product Name | Description | Unit Price | Bulk Price"
```

#### Multi-page Documents
```bash
# Process specific pages
python main.py multi-page-contract.pdf \
  --prompt "Focus on signature page - extract: signatory names, titles, dates, witness information"

# Summary extraction
python main.py annual-report.pdf \
  --prompt "Extract executive summary key points and financial highlights only"
```

### **Quality-Specific Processing**

#### High-Quality Scans
```bash
# Detailed extraction for clear documents
python main.py clear-scan.pdf \
  --prompt "Perform detailed extraction including: all text, formatting, table structure, footnotes"
```

#### Poor Quality Documents
```bash
# Focus on key information for unclear scans
python main.py blurry-document.jpg \
  --provider openai \
  --prompt "This is a poor quality scan. Extract the most important information: document type, date, key numbers"
```

#### Handwritten Documents
```bash
# Handwriting-specific prompts
python main.py handwritten-form.jpg \
  --prompt "This contains handwriting. Carefully transcribe: name, address, phone, signature date"
```

## 🔧 **Provider Selection for Documents**

### **By Document Type**

#### Complex Layouts (Tables, Multi-column)
```bash
# Use OpenAI for best accuracy
python main.py complex-layout.pdf \
  --provider openai \
  --prompt "Extract this complex multi-column document preserving layout structure"
```

#### Sensitive Documents (Medical, Legal, Financial)
```bash
# Use local processing for privacy
python main.py medical-record.pdf \
  --provider huggingface \
  --prompt "Extract patient information while maintaining confidentiality"
```

#### Bulk Processing (Cost-sensitive)
```bash
# Use SmolVLM for free bulk processing
python main.py invoice-batch/*.pdf \
  --provider huggingface \
  --prompt "Extract invoice number and total amount only"
```

## 📊 **Output Formatting**

### **JSON Structured Output**
```bash
# Business card to JSON
python main.py business-card.jpg \
  --prompt "Extract as JSON: {\"name\": \"\", \"title\": \"\", \"company\": \"\", \"email\": \"\", \"phone\": \"\", \"address\": \"\"}"

# Invoice to JSON
python main.py invoice.pdf \
  --prompt "Extract as JSON with fields: invoice_number, date, vendor, line_items (array), subtotal, tax, total"
```

### **CSV-Ready Output**
```bash
# Expense report processing
python main.py expense-receipts.jpg \
  --prompt "Extract as CSV format: Date,Vendor,Category,Amount,Tax,Total"

# Contact list extraction
python main.py contact-sheet.pdf \
  --prompt "Extract as CSV: Name,Title,Company,Email,Phone"
```

### **Summary Reports**
```bash
# Document summary
python main.py quarterly-report.pdf \
  --prompt "Provide a 3-sentence summary of key findings and recommendations"

# Contract summary
python main.py service-agreement.pdf \
  --prompt "Summarize: what services, duration, cost, key responsibilities of each party"
```

## 🚀 **Automation Workflows**

### **Batch Processing Script**
```bash
#!/bin/bash
# Process all PDFs in a directory
INPUT_DIR="documents"
OUTPUT_DIR="processed"

mkdir -p "$OUTPUT_DIR"

for doc in "$INPUT_DIR"/*.pdf; do
  filename=$(basename "$doc" .pdf)
  echo "Processing: $filename"
  
  python main.py "$doc" \
    --prompt "Extract: document type, date, key information, summary" \
    > "$OUTPUT_DIR/${filename}_extracted.txt"
done

echo "Batch processing complete!"
```

### **Document Classification**
```bash
# Auto-classify document types
python main.py unknown-document.pdf \
  --prompt "Classify this document type (invoice, contract, report, form, etc.) and extract the 3 most important pieces of information"
```

### **Data Validation**
```bash
# Extract and validate
python main.py form.pdf \
  --prompt "Extract all dates and verify they are in valid format. Extract all phone numbers and verify format. List any formatting issues found."
```

## 💡 **Pro Tips for Document Processing**

### **Optimize Your Prompts**
```bash
# Be specific about data format
python main.py document.pdf \
  --prompt "Extract dates in YYYY-MM-DD format, amounts with currency symbol, phone numbers with country code"

# Request error handling
python main.py unclear-scan.jpg \
  --prompt "If any text is unclear, mark with [UNCLEAR] and provide best guess in parentheses"
```

### **Handle Multiple Languages**
```bash
# Multilingual documents
python main.py multilingual-contract.pdf \
  --prompt "This document contains English and Spanish. Extract key terms and identify the language for each section"
```

### **Extract Metadata**
```bash
# Document information
python main.py signed-contract.pdf \
  --prompt "Extract: document title, creation date, last modified date, author, number of pages, signature status"
```

## 📈 **Quality Assurance**

### **Verification Workflow**
```bash
# Extract with confidence scoring
python main.py important-document.pdf \
  --prompt "Extract key information and indicate confidence level (high/medium/low) for each piece of data"

# Cross-verification with multiple providers
python main.py critical-contract.pdf --provider huggingface > hf_result.txt
python main.py critical-contract.pdf --provider openai > openai_result.txt
diff hf_result.txt openai_result.txt
```

### **Error Detection**
```bash
# Flag potential issues
python main.py document.pdf \
  --prompt "Extract information and flag any: missing signatures, blank required fields, inconsistent dates, unclear amounts"
```

## 🎯 **Real-World Examples**

### **Accounting Workflow**
```bash
# Monthly invoice processing
python main.py march-invoices/*.pdf \
  --prompt "Extract for accounting: vendor, invoice#, date, net amount, tax amount, total, GL account suggestions"
```

### **HR Document Processing**
```bash
# Resume screening
python main.py resume.pdf \
  --prompt "Extract: years of experience, key skills, education level, previous companies, contact info"

# Employee forms
python main.py employee-forms/*.pdf \
  --prompt "Extract: employee ID, name, department, start date, salary, benefits selections"
```

### **Legal Document Review**
```bash
# Contract comparison
python main.py contract-v1.pdf \
  --prompt "Extract key terms for comparison: parties, duration, payment terms, termination clauses"

python main.py contract-v2.pdf \
  --prompt "Extract key terms for comparison: parties, duration, payment terms, termination clauses"
```

## ⚠️ **Best Practices**

### **Privacy & Compliance**
- Use **SmolVLM** for sensitive documents (HIPAA, GDPR compliance)
- Never use **OpenAI** for confidential business data
- Always review extracted data before using in business processes

### **Accuracy Optimization**
- Use **OpenAI** for complex layouts and critical accuracy
- Try **multiple providers** for important documents
- **Validate extracted data** against original documents

### **Efficiency Tips**
- Use **specific prompts** to reduce processing time
- **Batch process** similar document types together
- **Cache results** to avoid reprocessing same documents

---

*Master these document processing techniques to transform your business document workflows with AI-powered text extraction!*
