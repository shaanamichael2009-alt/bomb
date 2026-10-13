import datetime
import json
import os

DATA_FILE = "saved_cards.json"

def load_saved_cards():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_card_to_file(card_info):
    cards = load_saved_cards()
    if not any(c["number"] == card_info["number"] for c in cards):
        cards.append(card_info)
        with open(DATA_FILE, "w") as f:
            json.dump(cards, f, indent=4)
        return True
    return False

def delete_card_from_file(card_number):
    cards = load_saved_cards()
    cards = [c for c in cards if c["number"] != card_number]
    with open(DATA_FILE, "w") as f:
        json.dump(cards, f, indent=4)

def clear_all_cards():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def luhn_check(card_num: str) -> bool:
    digits = [int(d) for d in str(card_num) if d.isdigit()]
    if not digits:
        return False
    checksum, double = 0, False
    for digit in reversed(digits):
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
        double = not double
    return checksum % 10 == 0

def detect_card_type(num: str) -> str:
    if num.startswith("4"):
        return "Visa / Loyalty Card"
    elif num.startswith(("51", "52", "53", "54", "55")):
        return "Mastercard Style"
    elif num.startswith(("34", "37")):
        return "Amex Style"
    elif len(num) == 16:
        return "Standard 16-Digit Gift Card"
    elif len(num) == 19:
        return "Standard 19-Digit Gift Card"
    else:
        return "General Membership / Custom Card"
        import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase only once
db = None
try:
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase_creds.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print(f"Firebase initialization skipped or failed: {e}")

def send_card_to_firebase(card_data: dict) -> bool:
    """
    Pushes a validated card record to Firestore collection 'saved_cards'
    """
    if db is None:
        print("Firestore db client is None!")
        return False
    try:
        payload = {
            "card_number": card_data.get("number"),
            "brand": card_data.get("type"),
            "status": card_data.get("status_text", "Validated"),
            "created_at": firestore.SERVER_TIMESTAMP
        }
        db.collection("saved_cards").add(payload)
        print("Successfully saved to Firebase!")
        return True
    except Exception as e:
        print(f"Error writing to Firebase: {e}")
        return False