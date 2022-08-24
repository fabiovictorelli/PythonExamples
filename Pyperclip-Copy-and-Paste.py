
# Working with Clipboard , Copy and Paste


import pyperclip

print('We had at our Clipboard :', pyperclip.paste())
pyperclip.copy('This is a Clipboard test ')
print('Now we have at our Clipboard :' + pyperclip.paste())
