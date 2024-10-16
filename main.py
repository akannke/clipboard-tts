import pyperclip
import time
from TTS.api import TTS
from playsound import playsound
import re

# TTSモデルをロード
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# クリップボードの初期状態を取得
previous_text = pyperclip.paste()

while True:
    try:
        # 現在のクリップボードの内容を取得
        current_text = pyperclip.paste()

        # 特殊文字を除外（通常の英語表現で使用する記号は残す）
        current_text = re.sub(r"[^\w\s'.,!?;:()-]", '', current_text)

        # クリップボードの内容が変更された場合
        if current_text != previous_text:
            previous_text = current_text

            # テキストが空でなく、1単語のみの場合に対処
            if current_text and len(current_text.split()) > 1:
                try: 
                    # テキストを音声に変換して保存
                    tts.tts_to_file(text=current_text, file_path="output.wav")
                    print("Text from clipboard was converted to speech and saved as 'output.wav'.")

                    # 音声ファイルを再生
                    playsound("output.wav")
                except Exception as e:
                    print(f"Error during TTS conversion or playback: {e}")
            elif len(current_text.split()) == 1:
                print("Single word detected. Skipping TTS conversion to avoid repetition.")
            else:
                print("Clipboard is empty.")

        # 1秒ごとにクリップボードをチェック
        time.sleep(1)

    except KeyboardInterrupt:
        # ユーザーが中断した場合、ループを終了
        print("Monitoring stopped.")
        break
