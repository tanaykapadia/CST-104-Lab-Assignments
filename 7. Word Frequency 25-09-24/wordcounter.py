with open('input.txt', 'r') as file:
    content = file.read()
file.close()

wordbreak = [' ', '\n', '\t', '.', ',', '!', '?', '/']
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
suffix = ["th", "st", "nd", "rd"]
times = ["am", "pm", "a.m.", "p.m."]

words = {}
wordslist = []
temp = ""
for char in content:
    if char in wordbreak:
        if temp != "":
            if temp[-1] == ':':
                temp = temp[:-1]
            wordslist.append(temp)
            if temp in words:
                words[temp] += 1
            else:
                words[temp] = 1
            temp = ""

            if len(wordslist) > 2:
                if wordslist[-1].isdigit() and wordslist[-2] in months and wordslist[-3][-2:] in suffix and wordslist[-3][:-2].isdigit():
                    newword = wordslist[-3] + ' ' + wordslist[-2] + ' ' + wordslist[-1]
                    words[wordslist[-1]] -= 1
                    words[wordslist[-2]] -= 1
                    words[wordslist[-3]] -= 1
                    wordslist.pop()
                    wordslist.pop()
                    wordslist.pop()
                    wordslist.append(newword)
                    if newword in words:
                        words[newword] += 1
                    else:
                        words[newword] = 1
            
            if len(wordslist) > 1:
                if wordslist[-1] in times and ':' in wordslist[-2]:
                    newword = wordslist[-2] + wordslist[-1]
                    words[wordslist[-1]] -= 1
                    words[wordslist[-2]] -= 1
                    wordslist.pop()
                    wordslist.pop()
                    wordslist.append(newword)
                    if newword in words:
                        words[newword] += 1
                    else:
                        words[newword] = 1

    else:
        if ord(char) in range(65, 91):
            temp += chr(ord(char) + 32)
        if (97 <= ord(char) <= 122) or (48 <= ord(char) <= 57) or (char == "'") or (char == "-") or (char=="$") or (char=="@") or (char=="&"):
            temp += char
        if char == ':':
            if len(temp) > 1 and temp[-1].isdigit():
                temp += char
        if not char.isdigit():
            if len(temp) > 1 and temp[-1] == ':':
                temp = temp[:-1]
        else:
            temp += char

if temp != "":
    if temp in words:
        words[temp] += 1
    else:
        words[temp] = 1

    if len(wordslist) > 2:
        if wordslist[-1].isdigit() and wordslist[-2] in months and wordslist[-3][-2:] in suffix and wordslist[-3][:-2].isdigit():
            newword = wordslist[-3] + ' ' + wordslist[-2] + ' ' + wordslist[-1]
            words[wordslist[-1]] -= 1
            words[wordslist[-2]] -= 1
            words[wordslist[-3]] -= 1
            wordslist.pop()
            wordslist.pop()
            wordslist.pop()
            wordslist.append(newword)
            if newword in words:
                words[newword] += 1
            else:
                words[newword] = 1
    
    if len(wordslist) > 1:
        if wordslist[-1] in times and ':' in wordslist[-2]:
            newword = wordslist[-2] + wordslist[-1]
            words[wordslist[-1]] -= 1
            words[wordslist[-2]] -= 1
            wordslist.pop()
            wordslist.pop()
            wordslist.append(newword)
            if newword in words:
                words[newword] += 1
            else:
                words[newword] = 1

wordfreq = []
for word in words:
    wordfreq.append((words[word], word))
wordfreq.sort()
wordfreq.reverse()

with open('output.txt', 'w') as file:
    for freq, word in wordfreq:
        file.write(f"{word}: {freq}\n")
file.close()