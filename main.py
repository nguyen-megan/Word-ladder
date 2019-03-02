import sys
#parse pair of words
def parse_pair(pair):
  return pair.split()

#use BFS search to find 
def build_Path(start, end, list_):
  queue = []
  #a list contain lists of path
  queue =[[start]]
  found = False
  #loop run until queue empty or target word is found
  while len(queue)>0:
    curr_list = queue[0]
    if curr_list.count(end) > 0:
      found = True
      break
    else:
      curr_word = curr_list[len(curr_list)-1]
      neighbors = find_neighbor(curr_word, list_)
      for y in neighbors:
        temp_list = curr_list.copy()
        temp_list.append(y)
        queue.append(temp_list)
    queue.pop(0)    
  if found:
    return curr_list
  else:
    return None

#return an updated list 
def same_length_words(target,list_):
  result = []
  length = len(target)
  for x in list_:
    if len(x) == length:
      result.append(x)
  return result

#find and return a list of matching val from dictionary
def find_neighbor (word, word_list):
  result1  =[]
  #if word_list contain word, get rid of it
  if(word_list.count(word) > 0):    
    word_list.remove(word)
  #for every word in list, check for their mismatch with target
  for x in word_list:
    mismatched = 0
    matched = True
    index = 0
    #go through each character in a word
    while index < len(word):
      #if mismatched between word and x is no more than 1 character, add to list of neighbor, and remove from list of word to search for
      if word[index] != x[index]:
        mismatched+=1
      if mismatched > 1:
        matched = False
      index +=1
    if matched:
      result1.append(x)
      word_list.remove(x)
  
  return result1

def main(argv):
  word_list = []
  pair_list = []

  #open and store word pairs into pair list
  file_1 = open("pairs.txt","r")
  pairs_file = file_1.readlines()
  for x in pairs_file:
    pair_list.append(x)
  file_1.close()

  #open and store big list of words into word list
  file_2 = open("dictionary.txt", "r")
  words_file = file_2.readlines()
  for x in words_file:
    x=x[:-1]
    word_list.append(x)
  file_2.close()

  #look at each pair in pair list
  for x in pair_list:
    temp = parse_pair(x)
    start = temp[0]
    end = temp[1]
    if(len(start)!= len(end)):
     print("No ladder from %s to %s"%(start,end))
    else:
      update_list = same_length_words(start, word_list)
      result = build_Path(start, end, update_list)
      if result != None:
        print(result)
      else:
        print("No ladder from %s to %s"%(start,end))
  pass

if __name__ == "__main__":
    main(sys.argv)