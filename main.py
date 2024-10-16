import pyperclip
from TTS.api import TTS
from playsound import playsound


# TTSモデルをロード
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# クリップボードからテキストを取得
text = pyperclip.paste()

# テキストを音声に変換して再生
if text:
    # Convert the clipboard text to speech and save it as an audio file named 'output.wav'
    tts.tts_to_file(text=text, file_path="output.wav")
    print("Text from clipboard was converted to speech and saved as 'output.wav'.")
    
    # Play the saved audio file
    playsound("output.wav")
else:
    # If the clipboard is empty, notify the user
    print("Clipboard is empty.")
