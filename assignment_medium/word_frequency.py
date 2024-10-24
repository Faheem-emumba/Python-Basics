# word frequency

# Open the file in read mode
with open('myFile.txt', 'r') as file:
    # Read the entire file content
    content = file.read()
    
    # Split the content into words
    words = content.split()
    
wordsFrequency={}    

# Print each word
for word in words:
    if word in wordsFrequency:
        wordsFrequency[word]=wordsFrequency[word]+1
    else:
        wordsFrequency[word]=1    

print(wordsFrequency)
