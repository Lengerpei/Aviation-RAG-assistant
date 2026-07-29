from rag import ask_question

print("=" * 60)
print("AVIATION GPT")
print("=" * 60)

print("Type 'exit' to quit.\n")

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer = ask_question(question)

    print("\nAnswer:\n")
    print(answer)