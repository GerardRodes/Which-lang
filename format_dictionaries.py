# -*- coding: utf-8 -*-

import os
import codecs


FOLDER = './dictionaries'
NUMBERS = [str(number) for number in range(10)]
CHARACTERS = [' ', '.', '-', '\'', '#', '!', '"', '·', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '|', '@', '#', '¬']
FORBIDDEN = [char for char in NUMBERS + CHARACTERS]



dictionaries = [dictionary for dictionary in os.listdir(FOLDER)
                if os.path.isfile( os.path.join(FOLDER, dictionary) ) and dictionary.endswith('.txt') ]

for dictionary in dictionaries:
  print( 'Formatting file {file}'.format(file = dictionary) )
  
  dictionary_filename = os.path.join(FOLDER, dictionary)
  temp_filename       = os.path.join(FOLDER, dictionary + '.temp')
  total_lines = sum(1 for line in open(dictionary_filename))
  
  with codecs.open(dictionary_filename, 'r', 'utf-8') as file:
    with codecs.open(temp_filename, 'w', 'utf-8') as temp_file:
      for index, line in enumerate(file):
        print( '{current}/{total}'.format(current = index + 1, total = total_lines) )
        
        if len( line.rstrip() ) > 3:
          forbidden_chars = [char for char in line if char in FORBIDDEN]
          
          if not forbidden_chars:
            formated_line = line.lower()
            temp_file.write(formated_line)
          
  os.remove(dictionary_filename)
  os.rename(temp_filename, dictionary_filename)