import tkinter as tk
import random
from gtts import gTTS
import os
from googletrans import Translator

class FlashcardApp:
def __init__(self, master):
self.master = master
self.master.title(&quot;English-Tamil Flashcards&quot;)

# Vocabulary data (English words and their Tamil translations)
self.vocab = {}

self.get_user_input()

self.current_pair = None
self.create_widgets()

def get_user_input(self):
# Get the number of word pairs the user wants to input
num_pairs = int(input(&quot;Enter the number of word pairs you want to input: &quot;))

# Get user input for each word pair
for _ in range(num_pairs):
english_word = input(&quot;Enter an English word: &quot;)
tamil_translation = self.translate_to_tamil(english_word)
self.vocab[english_word] = tamil_translation

def translate_to_tamil(self, english_word):
try:
translator = Translator()
translation = translator.translate(english_word, dest=&#39;ta&#39;)
return translation.text
except Exception as e:
print(f&quot;Translation error: {e}&quot;)
return &quot;Translation not available&quot;

def create_widgets(self):

self.canvas = tk.Canvas(self.master, width=400, height=200, bg=&quot;blue&quot;) # Set background color to
blue
self.canvas.pack(pady=20)

self.next_card()

self.btn_play_english_audio = tk.Button(self.master, text=&quot;Play English Pronunciation&quot;,
command=self.play_english_audio)
self.btn_play_english_audio.pack(pady=5)

self.btn_play_tamil_audio = tk.Button(self.master, text=&quot;Play Tamil Pronunciation&quot;,
command=self.play_tamil_audio)
self.btn_play_tamil_audio.pack(pady=5)

self.btn_next_card = tk.Button(self.master, text=&quot;Next Card&quot;, command=self.next_card)
self.btn_next_card.pack(pady=10)

def next_card(self):
self.current_pair = random.choice(list(self.vocab.items()))
self.show_flashcard()

def show_flashcard(self):
self.show_word()

def show_word(self):
self.canvas.delete(&quot;all&quot;)
english_word, tamil_translation = self.current_pair

display_text = f&quot;{english_word}\n({tamil_translation})&quot;
self.canvas.create_text(200, 100, text=display_text, font=(&quot;Helvetica&quot;, 14), fill=&quot;white&quot;) # Set text
color to white

def play_english_audio(self):
if self.current_pair:
english_word, _ = self.current_pair
generate_audio_spelling(english_word, language=&#39;en&#39;)

def play_tamil_audio(self):
if self.current_pair:
_, tamil_translation = self.current_pair
generate_audio_spelling(tamil_translation, language=&#39;ta&#39;)

def generate_audio_spelling(word, language=&#39;en&#39;):
try:
# Generate TTS audio for the given word and language
tts = gTTS(text=word, lang=language, slow=False)

# Save the audio file
audio_path = f&quot;{word}.mp3&quot;
tts.save(audio_path)

# Play the audio file
os.system(f&quot;start {audio_path}&quot;)

except Exception as e:
print(f&quot;Error: {e}&quot;)

def main():
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()

if __name__ == &quot;__main__&quot;:
main():