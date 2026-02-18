from pyscript import document, when  # type:ignore
from js import window  # type:ignore

# --- 1. Class แม่ ---
class Food:
    def __init__(self):
        self.sound_text = ""
        self.display_text = ""

    def describe(self):
        # สั่งให้ Browser พูด
        if self.sound_text:
            utterance = window.SpeechSynthesisUtterance.new(self.sound_text)
            utterance.lang = "th-TH"
            window.speechSynthesis.speak(utterance)
        return self.display_text


# --- 2. Class ลูก ---
class Pizza(Food):
    def __init__(self):
        self.sound_text = "พิซซ่าชีสเยิ้ม หอมอร่อยมาก"
        self.display_text = "🍕 พิซซ่าชีสเยิ้มพร้อมเสิร์ฟ!"

class Sushi(Food):
    def __init__(self):
        self.sound_text = "ซูชิสดใหม่จากทะเล"
        self.display_text = "🍣 ซูชิน่าทานมาก!"

class Burger(Food):
    def __init__(self):
        self.sound_text = "เบอร์เกอร์เนื้อฉ่ำๆ ร้อนๆ"
        self.display_text = "🍔 เบอร์เกอร์พร้อมทาน!"

class IceCream(Food):
    def __init__(self):
        self.sound_text = "ไอศกรีมหวานเย็นชื่นใจ"
        self.display_text = "🍨 ไอศกรีมเย็นๆ อร่อยสุดๆ!"


@when("click", "#btn_sound")
def play_sound(event):
    choice = document.getElementById("food_selector").value
    food = None
    
    if choice == "pizza": food = Pizza()
    elif choice == "sushi": food = Sushi()
    elif choice == "burger": food = Burger()
    elif choice == "icecream": food = IceCream()
    
    if food:
        text = food.describe()
        document.getElementById("output").innerText = text
