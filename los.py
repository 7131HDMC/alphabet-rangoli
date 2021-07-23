def print_rangoli(size):
    string= ''
    column =  ((size-1) * 4)+1
    line   = 1 +  (size-1) * 2
    #
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet[:size]
    los(size, alphabet)
    

def los(n, alphabet):
    m = n-1
    v = 1
    los = ''
    #
    for row in range(-m, m+1):
        #
        for col in range(-m, m+1):
            #
            if abs(row) + abs(col) <= m:
                #
                for t in range(0,m+1):
                    if abs(row) + abs(col) >= t:
                        c = alphabet[t]
                    elif abs(row) + abs(col) == t:
                        
                        c = alphabet[t]
                        # alphabet = alphabet.replace(c,'')
                        # if abs(col) > len(range(-m, m+1))//2:
                        #     c = 'e'
                        # else:
                        #     c = v 
                        break
                    elif abs(row) + abs(col) == m:
                        c = alphabet[t]
                        # alphabet = alphabet.replace(c,'')
                        break
            else:
                c = '-'                    
            los += c + '-'
        los = los[:-1] + '\n'
        v += 1
    print(los)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)