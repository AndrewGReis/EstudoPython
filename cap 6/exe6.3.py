def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

palavra = input("Digite uma palavra: ")
if is_palindrome(palavra):
    print("É palíndromo!")
else:
    print("Não é palíndromo!")