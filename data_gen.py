import ollama
import json
import time

# CAT 1: Algoritmi e Data Science 
cat_1 = [
      "Compare the time complexity of Merge Sort vs Quick Sort in best, average, and worst cases.",
    "Explain how Dijkstra’s algorithm finds the shortest path and where it fails compared to A*.",
    "Describe the role of heuristics in the A* algorithm and how to choose an admissible heuristic.",
    "What is Dynamic Programming and how does memoization improve performance?",
    "Explain the difference between BFS and DFS and when to use each.",
    "How does a Transformer architecture replace recurrence in sequence modeling?",
    "Describe how PCA reduces dimensionality and what variance preservation means.",
    "Explain the bias–variance tradeoff using a concrete example.",
    "What is overfitting and how does early stopping help prevent it?",
    "Compare bagging and boosting in terms of error reduction.",
    "Explain gradient descent and how learning rate scheduling affects convergence.",
    "What is the exploding gradient problem and how is it mitigated?",
    "Describe how convolution filters extract features in CNNs.",
    "How does dropout regularization help against overfitting?",
    "Explain KMeans and why it struggles with non-convex clusters.",
    "What is hierarchical clustering and how does linkage affect results?",
    "Describe the difference between L1 and L2 regularization.",
    "How do autoencoders compress information and what is a bottleneck layer?",
    "Explain the intuition behind word embeddings like Word2Vec.",
    "What is the difference between generative and discriminative models?",
    "How does a hash table achieve average O(1) access time?",
    "Describe binary search and why it requires a sorted list.",
    "What is the difference between a min-heap and a max-heap?",
    "Explain the Floyd–Warshall algorithm and its time complexity.",
    "What is a balanced binary tree and why is it important?",
    "Compare red–black trees and AVL trees.",
    "How does the PageRank algorithm evaluate importance of nodes?",
    "Explain TF-IDF and why it improves text relevance scoring.",
    "Describe the concept of Markov Chains and give a real-world example.",
    "What is a sliding window algorithm and where is it useful?",
    "Explain the concept of amortized time complexity with an example.",
    "Describe how LSTMs maintain long-term dependencies.",
    "What is the role of attention in sequence-to-sequence models?",
    "How does batch normalization stabilize training?",
    "Compare k-NN and SVMs for classification.",
    "Explain ROC curves and AUC.",
    "What is the curse of dimensionality?",
    "How does a Bloom Filter work and why can it have false positives?",
    "Explain the disjoint-set union (Union-Find) structure.",
    "Describe reservoir sampling and when it’s needed.",
    "What is a monotonic stack and where is it useful?",
    "Explain the Bellman-Ford algorithm and how it handles negative weights.",
    "What is the difference between supervised and unsupervised learning?",
    "Describe reinforcement learning and the concept of Q-learning.",
    "Explain the purpose of the softmax function.",
    "How do GANs train two networks in opposition?",
    "What is the difference between recall and precision?",
    "Explain entropy in the context of decision trees.",
    "Describe locality-sensitive hashing (LSH).",
    "What is a trie and why is it efficient for prefix queries?",
    # ... (Aggiungi variazioni su: Dijkstra, A*, Transformers, PCA, Overfitting, ecc.)
]

# CAT 2: Logica, Matematica e Probabilità
cat_2 = [
    "Explain the difference between a tautology and a contradiction.",
    "Solve for x: 2(x - 3) + 7 = 15.",
    "Describe the Monty Hall problem and why switching doors increases the probability of winning.",
    "Explain De Morgan’s Laws with examples.",
    "What is a logical implication and how does its truth table work?",
    "Solve for x: ln(x) + ln(3) = ln(12).",
    "Describe Russell’s paradox in simple terms.",
    "Explain the Prisoner’s Dilemma and its implications in game theory.",
    "What is a Nash equilibrium?",
    "Compute the derivative of f(x) = x^3 - 5x + 2.",
    "Explain the concept of a limit in calculus.",
    "What is an injective function and how does it differ from surjective?",
    "Describe the difference between permutations and combinations.",
    "A coin is flipped 10 times. What is the probability of getting exactly 6 heads?",
    "Explain conditional probability with an example.",
    "Describe a paradox and give a classical example.",
    "Explain the concept of mathematical induction.",
    "Show that sqrt(2) is irrational (conceptual explanation).",
    "What is the difference between discrete and continuous probability?",
    "Compute the integral ∫ (2x + 1) dx.",
    "Explain the concept of expected value.",
    "What is the gambler’s fallacy?",
    "Describe Gödel’s incompleteness theorem in simple terms.",
    "Explain what a bijection is.",
    "What is the difference between primes and composite numbers?",
    "Explain why division by zero is undefined.",
    "Solve for x: 3^(x+1) = 81.",
    "Describe the concept of entropy in information theory.",
    "Explain what a sigma-algebra is.",
    "What is a Markov property?",
    "Explain Bayesian inference in simple terms.",
    "A die is rolled twice. What is the probability the sum is 9?",
    "Explain what a matrix determinant represents.",
    "Compute the eigenvalues of a 2x2 matrix [[2,1],[1,2]].",
    "Explain the concept of proof by contradiction.",
    "Describe Zeno’s paradox.",
    "Explain what a graph is in discrete mathematics.",
    "What is the handshake lemma in graph theory?",
    "Solve for x: |3x - 7| = 5.",
    "What is a convergent series?",
    "Explain the difference between covariance and correlation.",
    "Describe the concept of variance.",
    "Explain what a random variable is.",
    "What is a paradox of implication?",
    "Solve the system: x + y = 10; x - y = 2.",
    "Explain the concept of a function limit approaching infinity.",
    "What is a logical XOR?",
    "Describe the halting problem.",
    "Explain the law of large numbers.",
    "What is a continuous random variable?",
    # ... (Aggiungi variazioni su: Paradossi logici, Teoria dei giochi, Calcolo integrale, ecc.)
]

# CAT 3: Programmazione Avanzata e Architettura
cat_3 = [
   "Explain the difference between horizontal and vertical scaling.",
    "What is a load balancer and how does it distribute traffic?",
    "Describe the CAP theorem and give real examples of each trade-off.",
    "Explain the difference between strong and eventual consistency.",
    "What is a distributed lock and why is it needed?",
    "Explain how Kubernetes handles container orchestration.",
    "Describe how gRPC uses HTTP/2 for performance.",
    "What is a consensus algorithm and why is it important?",
    "Explain the Raft algorithm in simple terms.",
    "What is the difference between synchronous and asynchronous communication?",
    "Describe how message queues improve system resilience.",
    "Explain how a CDN reduces latency.",
    "What is a microservices architecture and its main trade-offs?",
    "Describe circuit breaking and why it's used in distributed systems.",
    "Explain what an API Gateway does.",
    "Describe how Docker uses layered file systems.",
    "Explain what containerization solves compared to virtual machines.",
    "What is a service mesh and what problem does it solve?",
    "Explain sharding in databases.",
    "What is a NoSQL partition key and why is it important?",
    "Describe the master–slave replication model.",
    "Explain how Redis achieves in-memory fast reads.",
    "What is Kafka and why is it used?",
    "Describe backpressure in reactive systems.",
    "Explain the concept of idempotency in APIs.",
    "What is a deadlock and how can it occur in distributed systems?",
    "Describe optimistic vs pessimistic concurrency control.",
    "Explain how JWT authentication works.",
    "What is the difference between Bloom Filters and Cuckoo Filters?",
    "How do distributed transactions use two-phase commit?",
    "Explain what a reverse proxy does.",
    "What is serverless computing and its typical use cases?",
    "Describe the difference between monolithic and microservice deployments.",
    "Explain how autoscaling works in cloud environments.",
    "What is a sidecar container?",
    "Describe how hash rings work in consistent hashing.",
    "Explain what a stateful vs stateless service is.",
    "What is a gRPC streaming call?",
    "Why are immutable infrastructures easier to manage?",
    "Explain the concept of eventual consistency with an example.",
    "Describe how a distributed cache improves performance.",
    "What is a data lake?",
    "Explain map–reduce and where it is used.",
    "What is network partitioning and how systems handle it?",
    "Explain how IPv6 load balancing differs from IPv4.",
    "What is zero-downtime deployment?",
    "Describe rolling updates vs blue–green deployments.",
    "Explain memory management differences between Rust and C++.",
    "What is an event-driven architecture?",
    "Describe how observability differs from monitoring.",
    # ... (Aggiungi variazioni su: Docker, Kubernetes, Memory Management, Rust vs C++, ecc.)
]

all_questions = cat_1 + cat_2 + cat_3

ORGANIZATION = "DLTHA-LABS"
INPUT_QUESTIONS = all_questions

def generate_bulk_data():
    filename = 'dltha_reasoning_v1.jsonl'
    
    for i, question in enumerate(INPUT_QUESTIONS):
        print(f"[{i+1}/{len(INPUT_QUESTIONS)}] Processing: {question[:50]}...")
        
        try:
            # Prompt ingegnerizzato per il "Reasoning"
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
            
            # Un piccolo sleep per non stressare eccessivamente la memoria
            time.sleep(0.5) 
            
        except Exception as e:
            print(f"Error on question {i}: {e}")

if __name__ == "__main__":
    generate_bulk_data()