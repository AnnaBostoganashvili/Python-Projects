'''
Anna Bostoganashvili - Project 2 - DNA Identification
Dr. Bailey -- 11.03.2023
'''

# function to read the unknown sequence of DNA 
def read_unknown_sequence(dna, STR): 

    # accumulate number of the STR in the longest string
    max_counter = 0  
    for char_idx in range(len(dna)-len(STR)+1):  
        tandem_repeat = dna[char_idx : char_idx+len(STR)]  

        # counting the number of STR in each sequence 
        tandem_counter = 0 
        str_idx = char_idx 
        while tandem_repeat == STR:
            
            # adding the length of tandem repeat to the STR index
            tandem_counter += 1
            str_idx += len(STR)  
            tandem_repeat = dna[str_idx : str_idx+len(STR)]

        # if we find the bigggest amount of counts
        # max will become that biggest count
        if tandem_counter > max_counter: 
            max_counter = tandem_counter  
            
    # convert into string, because the others that we are
    # comparing to are list of string of numbers. 
    return str(max_counter) 

# Function for reading the entered database
def read_database(): 

    #open the file of the database 
    file = open("dna_db.csv", "r")
    # read the first line
    header_line = file.readline().strip().split(',')
    # make the list out of the first line of the STRs
    header_line = header_line[1 : len(header_line)]  

    # make the list of the names by using this accumulator 
    l_names = []
    # make the list of the list of repetitions (numbers)
    l_repetitions = []  
    new_line = file.readline().strip()

    # the reading of the file will end with the empty string.
    while new_line != "":   
        new_line = new_line.split(',')
        l_names.append(new_line[0]) 
        l_repetitions.append(new_line[1:len(new_line)]) 
        new_line = file.readline().strip() 

     # we will return all the three lists that we created above
    return header_line, l_names, l_repetitions


def main():
    # ask the user to input database
    file_name = input("Sequence file: ").strip() #.strip-removes spaces
    # open the database file
    file_fo = open(file_name, "r")  
    # read the database file
    read_file = file_fo.read() 
    dna = read_file.strip() # will remove "\n"     

    # call the second function 
    header_line, l_names, l_repetitions = read_database() 
    print(l_repetitions) 

    # number of STR repeats 
    l_counts = []  
    for str_repeat in header_line:
        l_counts.append(read_unknown_sequence(dna, str_repeat))
        
    print(l_counts)  

    # outside the range of the list
    index = -1  
    for i in range(len(l_repetitions)):
        # if the list of the cointed str match the
        # l_repetitions, then index will become i. 
        if l_counts == l_repetitions[i]: 
            index = i                    

    if index == -1: 
        print("No match")
    else: 
        print("Found match: ", l_names[index]) 


if __name__ == "__main__":
    main()
