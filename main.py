import argparse
import itertools

    
parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='argument', type=str, metavar='', required=True, help="Arguments icluded in the password. (E.g. Dogname, Wifes name, etc.) Seperate with a comma (',')!!")
args = parser.parse_args()

arguments = args.argument
arguments = arguments.replace(' ', '')
arguments = arguments.split(',')





def combination_gen(l, le):

    """Generates every possible combination of the Input-Arguments."""

    yield from itertools.product(*([l] * le)) 






def getSuffix():

    """This function returns all suffixes in the suff.txt file."""

    with open ('suff.txt', 'r', encoding="UTF8") as suff:
        suffix = suff.readlines()
        suf_full = ""
        
        for x in suffix:
            x = x.replace('\n', '')
            suf_full = suf_full + x + "\n"
      
            
    return suf_full
    
    
    
    
    
    
def getPrefix():

    """This function returns all prefixes in the pre.txt file."""

    with open ('pre.txt', 'r', encoding="UTF8") as pre:
        prefix = pre.readlines()
        
        pref_full = ""
        
        for x in prefix:
            x = x.replace('\n', '')
            pref_full = pref_full + x + "\n"
        
        
        return(pref_full)        
        
        
        
        
        

def generate_pass():

    """Generates every password possible with the given infromation (Arguments, Suffixes, Prefixes)"""


    counter_while = 1

    while (counter_while<=len(arguments)):
        
        suf_final = getSuffix()
        pre_final = getPrefix()
        
        suf_final = suf_final.split('\n')
        pre_final = pre_final.split('\n')
        
        combinations = combination_gen(arguments, counter_while)
                
        for x in combinations:
                
            for z in x:
                final_combination = ""
                final_combination = final_combination + z
                            
                for y in pre_final:
                    
                    for c in suf_final:
                        temp_pass = ""
                        temp_pass = str(y) + final_combination + str(c)
                        
                        with open('list.txt', 'a', encoding="UTF8") as list:
                            list.writelines(temp_pass + "\n")
                        list.close()

        counter_while = counter_while + 1
    





generate_pass()

