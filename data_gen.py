import ollama
import json
import time

# Read CAT_types.md to understand the CATS subjects 
# Example version of the code

cat_1 = [
    "Compare the time complexity of Merge Sort vs Quick Sort in best, average, and worst cases.",
    "Explain how Dijkstra’s algorithm finds the shortest path and where it fails compared to A*.",
    "Describe the role of heuristics in the A* algorithm and how to choose an admissible heuristic.",
]

cat_2 = [
    "Explain the difference between a tautology and a contradiction.",
    "Solve for x: 2(x - 3) + 7 = 15.",
]

cat_3 = [
   "Explain the difference between horizontal and vertical scaling.",
    "What is a load balancer and how does it distribute traffic?",
    "Describe the CAP theorem and give real examples of each trade-off.",
    "Explain the difference between strong and eventual consistency.",
    "What is a distributed lock and why is it needed?",
]

all_questions = cat_1 + cat_2 + cat_3

ORGANIZATION = "DLTHA-LABS"
INPUT_QUESTIONS = all_questions

def generate_bulk_data():
    filename = 'dltha_reasoning_v1.jsonl'
    
    for i, question in enumerate(INPUT_QUESTIONS):
        print(f"[{i+1}/{len(INPUT_QUESTIONS)}] Processing: {question[:50]}...")
        
        try:
            prompt = (f"Analyze the following problem, break it down into logical steps, "
                      f"and provide a final, verified answer. Question: {question}")
            
            response = ollama.chat(model='mistral', messages=[
                {'role': 'system', 'content': 'You are a PhD level assistant focused on technical accuracy and step-by-step logic.'},
                {'role': 'user', 'content': prompt},
            ])
            
            data = {
                "instruction": question,
                "thought_process": response['message']['content'],
                "metadata": {
                    "source": ORGANIZATION,
                    "batch": "v1_alpha",
                    "timestamp": time.time()
                }
            }
            
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(json.dumps(data) + '\n')
            
            time.sleep(0.5) 
            
        except Exception as e:
            print(f"Error on question {i}: {e}")

if __name__ == "__main__":
    generate_bulk_data()
