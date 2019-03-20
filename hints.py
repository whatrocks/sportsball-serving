
import random
facts = {
    'soccer': [
        'Ask what they thought about the goalie!',
        'Did you see that slide tackle?',
    ],
    'football': [
        'I stopped watching after the first touchdown',
        "What did you think of the quarterbacks?",
    ],
    'basketball': [
        'Those three pointers, tho!',
        'Everyone needs to work on their free throws, amirite?',
    ],
    'volleyball': [
        'Great serves!',
        'I dig 2x2 volleyball the best',
    ],
    'rugby': [
        'the pitch was so muddy!',
        'too many scrums!',
    ]
}

def fact_finder(label: str) -> str:
    return random.choice(facts[label])