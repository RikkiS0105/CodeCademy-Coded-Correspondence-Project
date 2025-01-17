#!/usr/bin/env python
# coding: utf-8

# # Casual Coded Correspondence: The Project
# 
# In this project, you will be working to code and decode various messages between you and your fictional cryptography enthusiast pen pal Vishal. You and Vishal have been exchanging letters for quite some time now and have started to provide a puzzle in each one of your letters.  Here is his most recent letter:
# 
#      Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a  Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. For example, if I chose an offset of 3 and a message of "hello", I would code my message by shifting each letter 3 places to the left (with respect to the alphabet). So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". Then I have my coded message,"ebiil"! Now I can send you my message and the offset and you can decode it. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer coded message that you have to decode yourself!
#     
#         xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
#     
#     This message has an offset of 10. Can you decode it?
#     
# 
# #### Step 1: Decode Vishal's Message
# In the cell below, use your Python skills to decode Vishal's message and print the result. Hint: you can account for shifts that go past the end of the alphabet using the modulus operator, but I'll let you figure out how!

# In[4]:


alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
def decode_caesars_message(message, offset):
    decoded_message = ""
    for a in message:
        if a in alphabet:
            temp_index = alphabet.index(a)
            if temp_index+offset <= 25:
                decoded_message += (alphabet[temp_index+offset])
            else:
                decoded_message += (alphabet[(temp_index+offset)%26])         
        else:
            decoded_message += a
    return decoded_message
            
            
                                       
coded_message = """xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"""
offset = 10

print(decode_caesars_message(coded_message, offset))

                                      


# #### Step 2: Send Vishal a Coded Message
# Great job! Now send Vishal back a message using the same offset. Your message can be anything you want! Remember, coding happens in opposite direction of decoding.

# In[7]:


def code_caesars_message(message, offset):
    recoded_message = ""
    for a in message:
        if a in alphabet:
            temp_index = alphabet.index(a)
            recoded_message += (alphabet[temp_index-offset])
        else:
            recoded_message += a
    return recoded_message

new_message_to_code = """wow! this was quite some work! spent half my day deciphering this!"""

print(code_caesars_message(new_message_to_code,10))

new_message_to_decode = "mem! jxyi mqi gkyju iecu meha! ifudj xqbv co tqo tusyfxuhydw jxyi!"
print(decode_caesars_message(new_message_to_decode, 10))




# #### Step 3: Make functions for decoding and coding 
# 
# Vishal sent over another reply, this time with two coded messages!
#     
#     You're getting the hang of this! Okay here are two more messages, the first one is coded just like before with  an offset of ten, and it contains the hint for decoding the second message!
#     
#     First message:
#     
#         jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.
#         
#     Second message:
#     
#         bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!
#     
# Decode both of these messages. 
# 
# If you haven't already, define two functions `decoder(message, offset)` and `coder(message, offset)` that can be used to quickly decode and code messages given any offset.

# In[10]:


first_message_to_decode = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
print(decode_caesars_message(first_message_to_decode,10))

second_message_to_decode = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

print(decode_caesars_message(second_message_to_decode, 14))


# In[11]:


def decode_without_offset(message):
    for a in range(len(alphabet)):
        print(decode_caesars_message(message,a))

#latest_message = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'        
#decode_without_offset(latest_message)



# #### Step 4: Solving a Caesar Cipher without knowing the shift value
# 
# Awesome work! While you were working to decode his last two messages, Vishal sent over another letter! He's really been bitten by the crytpo-bug. Read it and see what interesting task he has lined up for you this time.
# 
#             Hello again friend! I knew you would love the Caesar Cipher, it's a cool simple way to encrypt messages. Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? That's all changed with computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.
#             
#             To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of   the shift. You'll have to brute force it yourself.
#             
#             Here's the coded message:
#             
#             vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
#             
#             Good luck!
#             
# Decode Vishal's most recent message and see what it says!

# In[12]:


alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def decode_vignere_cipher(message, keyword):
    decoded_alphabet = ""
    special_character = 0
    
    for a in range(len(message)):
        b = a - special_character
        if message[a] in alphabet:
            temp_alpha1 = alphabet.index(message[a]) #index of the alphabet in message in alphabets list
            temp_alpha2 = b%(len(keyword))#index number of which alphabet in the keyword corresponds to 'a' - the alphabet being executed.
            temp_alpha3 = keyword[temp_alpha2] #the corresponding alphabet from the keyword
            temp_alpha4 = alphabet.index(temp_alpha3) #the index number of the alphabet in the keyword from the alphabets list
        
            shifted_alphabet_index = temp_alpha1 - temp_alpha4
            decoded_alphabet += alphabet[shifted_alphabet_index]
        else:
            decoded_alphabet += message[a]
            special_character += 1
    print(decoded_alphabet)
        
        
new_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword1 = "friends"

decode_vignere_cipher(new_message, keyword1)


        


# #### Step 5: The Vigenère Cipher
# 
# Great work! While you were working on the brute force cracking of the cipher, Vishal sent over another letter. That guy is a letter machine!
# 
#             Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. This next cipher I'm going to teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
#             
#            The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.
#            
#            Consider the message
#            
#                barry is the spy
# 
#            If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
#            
#                dog
#                
#            Now we use the repeat the keyword over and over to generate a _keyword phrase_ that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our _keyword phrase_ is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift the each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth. Remember, we zero-index because this is Python we're talking about!
# 
#                         message:       b  a  r  r  y    i  s   t  h  e   s  p  y
#                 
#                  keyword phrase:       d  o  g  d  o    g  d   o  g  d   o  g  d
#                  
#           resulting place value:       4  14 15 12 16   24 11  21 25 22  22 17 5
#       
#             So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth. Once we complete all the shifts we end up with our coded message:
#             
#                 eoxum ov hnh gvb
#                 
#             As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
#             
#                 dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!
#                 
#             and the keyword to decode my message is 
#             
#                 friends
#                 
#             Because that's what we are! Good luck friend!
#            
# And there it is. Vishal has given you quite the assignment this time! Try to decode his message. It may be helpful to create a function that takes two parameters, the coded message and the keyword and then work towards a solution from there.
# 
# **NOTE:** Watch out for spaces and punctuation! When there's a space or punctuation mark in the original message, there should be a space/punctuation mark in the corresponding repeated-keyword string as well! 

# In[14]:


def code_vignere_cipher(message, keyword):
    coded_alphabet = ""
    special_character = 0
    
    for a in range(len(message)):
        b = a - special_character
        if message[a] in alphabet:
            temp_alpha1 = alphabet.index(message[a]) #index of the alphabet in message in alphabets list
            temp_alpha2 = b%(len(keyword))#index number of which alphabet in the keyword corresponds to 'a' - the alphabet being executed.
            temp_alpha3 = keyword[temp_alpha2] #the corresponding alphabet from the keyword
            temp_alpha4 = alphabet.index(temp_alpha3) #the index number of the alphabet in the keyword from the alphabets list
        
            shifted_alphabet_index = (temp_alpha1 + temp_alpha4)%26
            coded_alphabet += alphabet[shifted_alphabet_index]
        else:
            coded_alphabet += message[a]
            special_character += 1
    #print(temp_alpha1, temp_alpha2, temp_alpha3, temp_alpha4, shifted_alphabet_index)
    print(coded_alphabet)

message = "its taken me 2 days to finish this assignment! i better get a job with raw after this!"
keyword = "black"

code_vignere_cipher(message,keyword)

message1 = "jes vklpn oo 2 elyu dp qipsts tjst lsushymgxu! t bgdupr iou l jql xttj bbh ahdfc tjst!"
decode_vignere_cipher(message1,keyword)


# #### Step 6: Send a message with the  Vigenère Cipher
# Great work decoding the message. For your final task, write a function that can encode a message using a given keyword and write out a message to send to Vishal!
# 
# *As a bonus, try calling your decoder function on the result of your encryption function. You should get the original message back!*

# In[ ]:





# #### Conclusion
# Over the course of this project you've learned about two different cipher methods and have used your Python skills to code and decode messages. There are all types of other facinating ciphers out there to explore, and Python is the perfect language to implement them with, so go exploring! 

#PUSHED TO GITHUB
