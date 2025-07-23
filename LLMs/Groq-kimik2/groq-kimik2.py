from groq import Groq
from dotenv import load_dotenv
import sys

sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
client = Groq()

completion = client.chat.completions.create(
    model="moonshotai/kimi-k2-instruct",
    messages=[
        {"role": "user", "content": "Me fale um pouco sobre n8n"}
    ],
    temperature=0.6,
    max_completion_tokens=4096,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
