from gtts import gTTS
from playsound import playsound
import asyncio

async def main():
    while True:
        text = input("enter text")

        speech = gTTS(text=text, lang='en', slow=False)

        speech.save("text.mp3")
        playsound("text.mp3")

        print(await main())

asyncio.run(main())
