import pyperclip
import time
from TTS.api import TTS
from playsound import playsound

# TTSモデルをロード
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# クリップボードの初期状態を取得
previous_text = pyperclip.paste()

while True:
    try:
        # 現在のクリップボードの内容を取得
        current_text = pyperclip.paste()

        # クリップボードの内容が変更された場合
        if current_text != previous_text:
            previous_text = current_text

            # テキストが空でない場合、TTSで再生
            if current_text:
                # テキストを音声に変換して保存
                tts.tts_to_file(text=current_text, file_path="output.wav")
                print("Text from clipboard was converted to speech and saved as 'output.wav'.")

                # 音声ファイルを再生
                playsound("output.wav")
            else:
                print("Clipboard is empty.")

        # 1秒ごとにクリップボードをチェック
        time.sleep(1)

    except KeyboardInterrupt:
        # ユーザーが中断した場合、ループを終了
        print("Monitoring stopped.")
        break
