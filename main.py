from openai import OpenAI
from pathlib import Path
import os

client = OpenAI(api_key=os.environ["OPENAI_KEY"])

VOICES = {
    "alloy": "androgynous, soft",
    "echo": "male, soft",
    "fable": "male, soft, british accent",
    "onyx": "male, grizzly",
    "nova": "female, soft, adult",
    "shimmer": "female, soft, middle aged",
}

def estimate_cost(string, per_char):
    one_K_units = len(string) / 100
    return one_K_units * per_char

def main():

    book_file = "ShadowSlave_Ch1.txt"

    with open(book_file, "r") as fh:
        book_lines = fh.readlines()

    book_str = "\n".join(book_lines)

    speech_file_path = Path(__file__).parent / "speech.mp3"

    snippet = book_str[:1000]
    
    sys_msg1 = """You are a text classification expert. 
    Given a section of text from a book extract the character / narrator dialogue section.
    All text should be perfectly preserved without anything changed, only classifying who says what.
    For example the input: \"Walking the dog Janice shouted \'\Here Boy!'. Soon after a black labrador ran through the open field\"
    Provides the output in the following format marking the speaker with *!*SPEAKER*!*:
    *!*Narrator*!* "Walking the dog Jance shouted"
    *!*Janice!*!* "Here Boy!"
    *!*Narrator*!* "Soon after a black labrador ran through the open field"
    """

    client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system","content": sys_msg1},
            {"role": "user"  ,"content": snippet},
        ]
    )

    # response = client.audio.speech.create(
    #     model="tts-1",
    #     voice="onyx",
    #     input=snippet
    # )

    # response.stream_to_file(speech_file_path)

main()