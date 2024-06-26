import whisper

model = whisper.load_model("small")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
audio_path = "./greeting_1.wav"
transcription = transcribe_audio(audio_path)
print ("Transcription: ", transcription)