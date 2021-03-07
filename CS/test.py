def re(srt,spc,rows):
    if srt > rows :
        pass
    elif srt== rows:
         print("*" * 10,srt,spc) 
    else :
        print("*" * srt," " * (spc-2),"*" * srt,srt,spc) 
        re(srt+1,spc-2,rows)
        print("*" * srt," " * (spc-2),"*" * srt,srt,spc)
     
re(1,8,5)