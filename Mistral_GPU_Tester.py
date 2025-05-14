from llama_cpp import Llama

llm = Llama(
    model_path=r"C:\Users\shiny\Downloads\AI\mistral-7b-instruct-v0.1.Q4_K_M.gguf", 
    n_ctx=2048,
    verbose=True
)

while True:
    prompt = input("You: ")
    output = llm.create_completion(prompt=prompt, max_tokens=256, stop=["</s>"])
    print("Mistral:", output["choices"][0]["text"].strip())
