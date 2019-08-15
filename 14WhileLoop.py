
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

print("#####################Building a Guessing Game###################")

secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win")

print("#####################Building a Guessing Game###################")

secretword = "giraffe"
guess1 = ""
guess1_count = 0
guess1_limit = 3
out_of_guesses = False

while guess1 != secretword and not(out_of_guesses):
    if guess1_count < guess1_limit:
        guess1 = input("Enter guess: ")
        guess1_count += 1
    else:

        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You lose")
print("You win")