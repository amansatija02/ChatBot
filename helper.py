def clean_input(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be string")
    return text.strip()