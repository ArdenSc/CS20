# CS20
# Arden Sinclair
# Jan 16, 2020
# Prints out formatted words and definitions


glossary = {
    'list': 'an ordered data structure holding a sequence of items',
    'dictionary': 'a data structure that has key and value pairs',
    'function': 'a reusable block of code that performs an action and '
                'returns a result',
    'abstraction': 'a strategic removal of details to simplify the process '
                   'for achieving a goal',
    'algorithm': 'an order of actions for performing a task or solving a '
                 'problem',
    'print function': 'a function in Python that writes text to the console',
    'for loop': 'a loop that performs an action for each value in a list, '
                'dictionary, range, string, or other compound data structure',
    'while loop': 'a loop that performs an action repeatedly as long as a '
                  'given condition evaluates to true',
    'if statement': 'a control statement in Python that runs a block of code '
                    'once if the condition is true',
    'else statement': 'a control statement in Python that runs a block of '
                      'code if all previous if and elif statements in an '
                      'if..elif block evaluate to false'
}

for k, v in glossary.items():
    print(f"{'An' if k[0] in ['a', 'e', 'i', 'o', 'u'] else 'A'} {k} is"
          f" {v}.\n")
