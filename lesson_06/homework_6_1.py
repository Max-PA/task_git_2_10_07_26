# Incoming sentence from user
sentence_to_analyze = input("Enter your sentence: ")

# Display user input
print(f'Користувач ввів речення: {sentence_to_analyze}')

# London is the capital of Great Britain

# Convert the string to a set and count unique characters
unique_symbols_in_sentence = len(set(sentence_to_analyze))
print(f'кількість унікальних символів у реченні складає: {unique_symbols_in_sentence}')

# outputting True to the console if len > 10, otherwise - False
if unique_symbols_in_sentence > 10:
    print(True)
else:
    print(False)

