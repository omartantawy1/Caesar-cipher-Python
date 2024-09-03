

from art import logo

print(logo)

should_end=False

while not should_end:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #it used to skip if i write shift numbers more than the text
  shift=shift%26

  def caesar(cipher_direction,start_text,shift_amount):
      end_text=''
      if cipher_direction=='decode':
        shift_amount*=-1
      for char in start_text:
        if char in alphabet:
          position=alphabet.index(char)
          new_position=position+shift_amount 
          end_text+=alphabet[new_position]
        else:
          end_text+=char
      print(f"the {cipher_direction}d text is {end_text} ")  
      result=input('do u want to end the game ? : ')
      if result=='yes':
        should_end==True
      
  caesar(cipher_direction=direction,start_text=text,shift_amount=shift)  

