def anagram(input_string):
    if len(input_string)%2 != 0:
        return -1
    else:
        cnt = 0
        no_chr = [0]*26
        
        # Splitting string
        s1 = input_string[:len(input_string)//2]
        s2 = input_string[len(input_string)//2:]
        
        for i in range(26):
            no_chr[i] = 0
            
        for i in range(len(s1)):
            no_chr[ord(s1[i]) - ord('a')] += 1
        
        for i in range(len(s2)):
            no_chr[ord(s2[i]) - ord('a')] -= 1
            if (no_chr[ord(s2[i]) - ord('a')] < 0):
                cnt += 1
                
        return cnt
  

def main():
    no_of_changes_for_anagram = anagram('anna')
    print('Number of changes for anagram: {0}\n'.format(no_of_changes_for_anagram))

if __name__ == '__main__':
    main()
