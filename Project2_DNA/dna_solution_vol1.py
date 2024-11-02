'''
Anna Bostoganashvili -- DNA Identification
'''

# Function to read the unknown sequence of DNA 
def read_unknown_sequence(dna, STR): # the parameters must not match necessarily, is is

    max_counter = 0  # counting the number of the str in the longest string #just the place holder. 
    for char_idx in range(len(dna)-len(STR)+1): # it is going to include everything in dna except for the last few 
        tandem_repeat = dna[char_idx : char_idx+len(STR)] # the tandem repeat will be from the beginning to the length of the str 

        tandem_counter = 0 # counting the number of tandem repeat in each sequence 
        str_idx = char_idx 
        while tandem_repeat == STR: # while it is equal then, we start counting from
                                #the first character str_idx of that str until the whole lenght. and then
                                # add up the amount. 
            tandem_counter += 1
            str_idx += len(STR) # we are adding the length of tandem repeat to the str index ??? 
            tandem_repeat = dna[str_idx : str_idx+len(STR)]

        if tandem_counter > max_counter: # if we find the bigggest amount of counts max will become that biggest count
            max_counter = tandem_counter # even if there are 5 different sequences, when it is going through, and countr
            # 4 different ssequences, first startig from first str_index, then second, then third, and it will make all
            # the 4 sequences, it will still choose the BIGGEST which is 5. 
            
    return str(max_counter) #convert this into string, because the others that we are comparing to are list of string of numbers 


def read_database(): #have the parameter as the file name
#this is hard coded - this is what we want it to look like if the user eters another sequence, or is just irregular 
##    l_STRs = ["AGAT", "AATG", "TATC"]
##    l_names = ["Alice", "Bob", "Charlie"]
##    l_repetitions = [[5,2,8], [3,7,4], [6,1,5]]

    file = open("dna_db.csv", "r") #open the file of the database 
    header_line = file.readline().strip().split(',') # read the first line - remove the empty space from the beginning and end. Split - convert into list, by turning all the elemtents into strings 
    header_line = header_line[1 : len(header_line)] # make the list out of the first line of the strs 

    l_names = [] # make the list of the names by using this accumulator 
    l_repetitions = [] # make the list of the list of repetitions (numbers) 
    new_line = file.readline().strip() # 
    while new_line != "": # the reading of the file will end with the empty string. So until we have not reached the end yet be in this loop 
        new_line = new_line.split(',')
        l_names.append(new_line[0]) # we can append the list without assigning new variable. Adding to the list the first thing in the text, because names are the first things in the text of each line 
        l_repetitions.append(new_line[1:len(new_line)]) # for strings we need new variable. Adding the first index till the end of the string because index 0 is names that we have above. 
        new_line = file.readline().strip() # it will return empty string when we are done. So this will be the end of the loop 

    return header_line, l_names, l_repetitions # we will return all the three lists that we created above


#def sequence_in_database():


def main():
    # asking the user to input the string of dna.
    file_name = input("Sequence file: ").strip() # this will get rid of spaces, that user desides to put in not to result in problems later on
    file_fo = open(file_name, "r") # open the database file 
    read_file = file_fo.read() # read the database file - the whole file will be read 
    dna = read_file.strip() # will remove \n    # this will be our dna strand to work with, that will go into the first function 

    header_line, l_names, l_repetitions = read_database() # calling the second function 
    print(l_repetitions) # printing the repetitions which is the list of list of numbers 

    l_counts = [] # number of counts of str repeats 
    for str_repeat in header_line:
        l_counts.append(read_unknown_sequence(dna, str_repeat)) #calling the function to make compare the str_repets in the header line, those three specifics that are given. To put these in the first
                                                                # function and substitute instead of STR. 
    print(l_counts) # so this will give us the list of the number of those 3 strs that are in the dna string 

    index = -1 # if it is outside the range of the list 
    for i in range(len(l_repetitions)): 
        if l_counts == l_repetitions[i]: # if the list of the cointed str match the l_repetitions, then index will become i. When index was outside the range, i is inside the range, so it will be 
            index = i                    # so it will not print "no match" "no match" then Alice, instead it will print just alice 

    if index == -1: 
        print("No match")
    else: 
        print("Found match: ", l_names[index]) # we cannot write the i here instead of the index, because i is in the for loop that we left, but index became i, so we can write it here

        

if __name__ == "__main__":
    main()
