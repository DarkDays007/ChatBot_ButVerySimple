import re

# Λίστα με τα πρότυπα προτάσεων και τις αντίστοιχες απαντήσεις
patterns_res = [
    (r'hello', 'Hello! How can I help you?'),
    (r'how are you', 'I am doing well, thank you!'),
    (r'what is your name', 'My name is Chatbot.'),
    (r'i need (.*)', 'Why do you need {0}?'),
    #συζητηση για θεμα που καποιος εχει προβλημα στην σχεση του  
    #Άνθρωπος: Λοιπόν, ο φίλος μου με έκανε να έρθω εδώ.
#ELIZA: Ο φίλος σου σε έκανε να έρθεις εδώ;
#Άνθρωπος: Λέει ότι έχω κατάθλιψη πολλές φορές.
#ELIZA: Λυπάμαι που ακούω ότι είστε σε κατάθλιψη.
#Άνθρωπος: Είναι αλήθεια. Δεν είμαι χαρούμενος.
#ELIZA: Πιστεύεις ότι το να έρθεις εδώ θα σε βοηθήσει να μην είσαι δυστυχισμένος;

    (r'Well, my boyfriend made me come here','Your boyfriend made you come here?'),
    (r'He says Im depressed much of the time.', ' am sorry to hear you are depressed.'),
    (r'Its true. I am unhappy.','Do you think coming here will help you not to be unhappy?'),
    (r'I Dont know what to do','Well sometimes we have to do nothing just stay '),
    (r'Why','Sometimes we shouldnt look for reasons in events'),
    (r'What would you suggest','Go and talk with all your feelings and dont forget that nothing is more important than you '),

    #γενικες συζητησεις 
    (r'What can i do','Sometimes the best thing you can do is just keep going and dont think so much '),
    (r'i dont know what to do ','When you dont know what to do it can be good to ask someone who is older or knowledgeable from you '),
    (r'Thank you ','You are welcome'),
    (r'Byee','See you laterrr'),



    # Προσθέστε εδώ περισσότερα πρότυπα προτάσεων και απαντήσεις ανάλογα με τις απαιτήσεις
]

def chatbot(input_sentence):
    for pattern, resp in patterns_res:
        if re.search(pattern, input_sentence):
            return re.sub(pattern, resp, input_sentence)
    return "I am not sure I understand. Can you please rephrase?"

# Εκκίνηση της συζήτησης
print("Welcome to the Chatbot!")
print("You can start chatting. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        print("Chatbot:", chatbot(user_input))
