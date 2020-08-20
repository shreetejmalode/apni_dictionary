# create a dictionary and take input from the user and return the meaning of the word from dictionary
# word from dictonary

Dic={
    'mutable' : 'liable to change.',
    'immutable' : 'unchanging over time or unable to be changed.',
    'python programming' :'Python is an interpreted, high-level, general-purpose programming language',
    'math' : 'The research required to solve mathematical problems can take years or even centuries of sustained inquiry.',
}

user_name = input("enter a word : ")
print(Dic[user_name])
