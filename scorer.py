def judge(question: str, expects: str, answer: str, results) -> bool:
    """
    Judge the answer of a question.

    Args:
        question (str): The question to be judged.
        expects (str): The expected answers.
        answer (str): The answer to be judged.
        results (str): The results of the judge.

    Returns:
        bool: True if the answer is correct, False otherwise.
    """
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()


