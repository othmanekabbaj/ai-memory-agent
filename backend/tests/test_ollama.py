from llm.ollama_client import OllamaClient

print("Creating client...")
client = OllamaClient()

print("Sending request...")
response = client.chat("Reply with exactly the word: hello")

print("Received:")
print(response)