import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for index, questions in enumerate(data):
    index = index + 1
    print(f"Question-{index}", questions["question_text"])
    [print(f"{inside_index+1}-{i}") for inside_index, i in enumerate(questions["options"])]
    # print(f"Correct Answer", questions["correct_answer"])
    user_actions = int(input("Enter your answer: "))
    questions["user_answer"]= user_actions

score = 0
for index, final_output in enumerate(data):
    if (final_output["correct_answer"] == final_output["user_answer"]):
        print(f" {index + 1} Correct Answer: User Answer: {final_output["user_answer"]}, Correct Answer: {final_output["correct_answer"]}")
        score += 1
    else:
        print(
            f" {index + 1} Wrong Answer: User Answer: {final_output["user_answer"]}, Correct Answer: {final_output["correct_answer"]}")

print(f"Score {score}/{len(data)}")
