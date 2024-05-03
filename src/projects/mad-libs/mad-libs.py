def get_input(word_type: str) -> str:
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


noun1: str = get_input("noun")
verb1: str = get_input("verb")
noun2: str = get_input("noun")
verb2: str = get_input("verb")


story: str = f"""
Once upon a time, there was a {noun1} who loved to {verb1} all day.
One day, the {noun1} met a {noun2} who also loved to {verb1}.
The two of them would {verb1} and {verb2} together every day.
"""

print(story)
