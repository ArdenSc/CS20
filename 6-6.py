poll_taken = {
    'Arden': True,
    'Aunglay': False,
    'Huy': False,
    'Evan': True
}

for k, v in poll_taken.items():
    if v:
        print(f"{k}, thank you for taking the poll.")
    else:
        print(f"{k}, please fill out the poll.")
