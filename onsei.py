import math
import whisper
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# TODO
output_filename = "output.lrc"

# モデルのロード
model = whisper.load_model("medium")

# 文字起こし対象のファイルを選択
result = model.transcribe("")

# 詳細な結果の表示
with open(output_filename, "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        if segment['start'] >= 60:
            start_minutes = math.floor(segment['start'] / 60)
            start_seconds = segment['start'] % 60
            formatted_start_time = f"{start_minutes:02}:{start_seconds:05.2f}"

        else:
            formatted_start_time = f"{00:02}:{segment['start']:05.2f}"
        output_line = f"[{formatted_start_time}]{segment['text']}"
        f.write(output_line + "\n")
