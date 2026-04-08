# ===============================
# 📌 LLM Robustness Evaluation Project
# ===============================

import random
import matplotlib.pyplot as plt

# ===============================
# 📊 1. Accuracy Function
# ===============================
def calculate_accuracy(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / len(actual)


# ===============================
# 🔄 2. Code-Mixing Generator
# ===============================
hindi_words = {
    "good": "accha",
    "bad": "bura",
    "very": "bahut",
    "movie": "film",
    "is": "hai"
}

def code_mix(sentence, prob=0.3):
    words = sentence.split()
    new_sentence = []

    for word in words:
        if word.lower() in hindi_words and random.random() < prob:
            new_sentence.append(hindi_words[word.lower()])
        else:
            new_sentence.append(word)

    return " ".join(new_sentence)


# ===============================
# 📂 3. Dataset Creation
# ===============================
def create_datasets(base_dataset):
    datasets = {}

    datasets["monolingual"] = base_dataset

    datasets["light"] = [(code_mix(text, 0.2), label) for text, label in base_dataset]
    datasets["medium"] = [(code_mix(text, 0.5), label) for text, label in base_dataset]
    datasets["heavy"] = [(code_mix(text, 0.8), label) for text, label in base_dataset]
    datasets["multilingual"] = [(code_mix(text, 0.6), label) for text, label in base_dataset]

    return datasets


# ===============================
# 🤖 4. Dummy Model Prediction
# ===============================
def predict(text):
    text = text.lower()

    if "good" in text or "accha" in text:
        return "Positive"
    elif "bad" in text or "bura" in text:
        return "Negative"
    else:
        return "Neutral"


# ===============================
# ⚙️ 5. Evaluation Function
# ===============================
def evaluate(dataset):
    actual = []
    predicted = []

    for text, label in dataset:
        actual.append(label)
        predicted.append(predict(text))

    return calculate_accuracy(actual, predicted)


# ===============================
# 📊 6. Main Execution
# ===============================
if __name__ == "__main__":

    # Base dataset (sample)
    base_dataset = [
        ("This movie is very good", "Positive"),
        ("This movie is bad", "Negative"),
        ("It is okay", "Neutral"),
        ("The product is very good", "Positive"),
        ("This is very bad", "Negative"),
        ("Average experience", "Neutral")
    ]

    # Create datasets
    datasets = create_datasets(base_dataset)

    results = {}

    print("\n📊 Accuracy Results:\n")

    for name, data in datasets.items():
        acc = evaluate(data)
        results[name] = acc
        print(f"{name.capitalize()} Dataset Accuracy: {acc:.2f}")

    # ===============================
    # 📈 7. Plot Graph
    # ===============================
    names = list(results.keys())
    values = list(results.values())

    plt.plot(names, values, marker='o')
    plt.xlabel("Dataset Type")
    plt.ylabel("Accuracy")
    plt.title("Accuracy vs Code-Mixing")
    plt.show()
