import json

def test_question_loading():
    with open("questions.json", "r") as file:
        questions = json.load(file)
    assert len(questions) > 0

def test_question_structure():
    with open("questions.json", "r") as file:
        questions = json.load(file)

    for q in questions:
        assert "question" in q
        assert "options" in q
        assert "answer" in q
        assert len(q["options"]) == 4

def test_score_logic():
    score = 0
    selected_answer = "Delhi"
    correct_answer = "Delhi"

    if selected_answer == correct_answer:
        score += 1

    assert score == 1

def test_answer_validation_wrong():
    score = 0
    selected_answer = "Mumbai"
    correct_answer = "Delhi"

    if selected_answer == correct_answer:
        score += 1

    assert score == 0