

from transformers import pipeline

generator = pipeline('text-generation',model = 'gpt2',pad_token_id = 50256,framework = 'pt',truncation = True)

prompt = input("Enter a prompt:")

results = generator(prompt, max_length = 80, num_return_sequences = 1)


for i, result in enumerate(results):
    print(f"\nGenerated text {i+1}:\n{result['generated_text']}")
    
    
