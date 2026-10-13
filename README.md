# CardValidator Pro 💳

**The most secure and private way to verify gift cards and membership cards.**

Advanced OCR technology combined with Luhn algorithm validation—all running locally on your device. No cloud, no tracking, no compromises.

---

## 🚀 Features

- ✅ **Smart OCR Technology** - Extract card numbers from images automatically
- ✅ **Instant Validation** - Real-time Luhn algorithm verification
- ✅ **Zero Cloud Storage** - 100% local processing, your data never leaves your device
- ✅ **Smart Detection** - Automatically identifies card types (Visa, Mastercard, gift cards, etc.)
- ✅ **Secure Vault** - Save and manage validated cards locally
- ✅ **Beautiful UI** - Modern, responsive interface with smooth animations

---

## 📋 Prerequisites

### Required Software

1. **Python 3.8+**
   - Download from: https://www.python.org/downloads/

2. **Tesseract OCR** (Required for image scanning feature)
   - **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

---

## 🛠️ Installation

### Step 1: Clone or Download the Project

```bash
cd c:\xampp\htdocs\bomb
```

### Step 2: Install Python Dependencies

```bash
pip install streamlit opencv-python pytesseract pillow numpy
```

### Step 3: Install Tesseract OCR

#### Windows Installation:

1. Download the installer: [tesseract-ocr-w64-setup](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the `.exe` installer
3. Note the installation path (usually `C:\Program Files\Tesseract-OCR`)
4. **Add to PATH** or configure manually:

If Tesseract is not in your PATH, you can set it manually by editing `pages/home.py`:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

#### macOS Installation:

```bash
brew install tesseract
```

#### Linux Installation:

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

---

## 🎯 Running the Application

### Start the Streamlit Server:

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 📖 How to Use

### 1. **Landing Page**
   - Click "🚀 Launch CardValidator" to enter the app

### 2. **Manual Entry Mode**
   - Enter card number manually
   - Select card brand/type
   - Click "🔍 Validate Card"
   - Save to vault if needed

### 3. **OCR Image Upload Mode**
   - Upload a clear photo of your card
   - OCR engine extracts numbers automatically
   - Review detected cards and save them

### 4. **Vault**
   - View all saved cards
   - Search and filter by type
   - Export as JSON
   - Delete individual cards or clear all

---

## 🔧 Troubleshooting

### OCR Error: "tesseract is not installed"

**Solution:**
- Install Tesseract OCR (see installation steps above)
- Add Tesseract to your system PATH
- Or set the path manually in the code

### "Module not found" errors

**Solution:**
```bash
pip install --upgrade streamlit opencv-python pytesseract pillow numpy
```

### Image not scanning properly

**Solution:**
- Ensure the card image is clear and well-lit
- Try taking a photo with better contrast
- Use Manual Entry mode as an alternative

---

## 🔐 Privacy & Security

**CardValidator Pro is 100% client-side:**
- All processing happens on YOUR device
- No data is sent to external servers
- No tracking, no analytics, no cloud storage
- Your card data is stored locally in `saved_cards.json`

---

## 🛡️ Supported Card Types

- Amazon Gift Cards
- Apple / iTunes Cards
- Visa Prepaid
- Mastercard Prepaid
- Steam Wallet
- Google Play
- Target Gift Cards
- Starbucks Cards
- Loyalty & Membership Cards
- Custom 16-19 digit formats

---

## 📚 Tech Stack

- **Python** - Core language
- **Streamlit** - Web framework
- **Tesseract OCR** - Image text extraction
- **OpenCV** - Image processing
- **PIL (Pillow)** - Image manipulation
- **NumPy** - Numerical operations
- **Luhn Algorithm** - Card validation

---

## 📝 Project Structure

```
bomb/
├── app.py                  # Main entry point & backend engine
├── landing.py              # Landing page
├── pages/
│   ├── home.py            # Validator dashboard
│   ├── vault.py           # Saved cards manager
│   └── about.py           # Info & features page
├── saved_cards.json       # Local storage (auto-generated)
└── README.md              # This file
```

---

## 🤝 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review error messages in the app
3. Ensure all dependencies are installed correctly

---

## ⚖️ License

This project is for educational and personal use. Handle card data responsibly.

---

## 🎉 Enjoy!

CardValidator Pro puts you in control. Validate cards securely, privately, and effortlessly! 🚀
