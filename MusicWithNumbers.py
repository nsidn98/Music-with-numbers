from pysynth import pysynth
import numpy as np

######################## Scales ###########################

C_major_pent={0:['c3',1],1:['d3',1],2:['e3',2],3:['g3',2],4:['a3',3],\
              5:['c4',3],6:['d4',4],7:['e4',4],8:['g4',5],9:['a4',5]}

# C# pentatonic: C#, D#, F, G#, A#, C#
C_sharp_pent={0:['c#3',1],1:['d#3',1],2:['f3',2],3:['g#3',2],4:['a#3',3],\
              5:['c#4',3],6:['d#4',4],7:['f4',4],8:['g#4',5],9:['a#4',5]}

# D# pentatonic: Db, Eb, F, Ab, Bb, Db
D_sharp_pent={0:['d#3',1],1:['e#3',1],2:['f3',2],3:['a#3',2],4:['b#3',3],\
            5:['d#4',3],6:['e#4',4],7:['f4',4],8:['a#4',5],9:['b#4',5]}

#D pentatonic: D, E, F#, A, B, D
D_pent={0:['d3',1],1:['e3',1],2:['f#3',2],3:['a3',2],4:['b3',3],\
        5:['d4',3],6:['e4',4],7:['f#4',4],8:['a4',5],9:['b4',5]}

#Eb pentatonic: Eb, F, G, Bb, C, Eb
E_sharp_pent={0:['e#3',1],1:['f3',1],2:['g3',2],3:['b3',2],4:['c3',3],\
            5:['e#4',3],6:['f4',4],7:['g4',4],8:['b4',5],9:['c4',5]}

# E pentatonic: E, F#, G#, B, C#, E
E_pent={0:['e3',1],1:['f#3',1],2:['g#3',2],3:['b3',2],4:['c#3',3],\
               5:['e4',3],6:['f#4',4],7:['g#4',4],8:['b4',5],9:['c#4',5]}

# F pentatonic: F, G, A, C, D, F
F_pent = {0:['f3',1],1:['g3',1],2:['a3',2],3:['c3',2],4:['d3',3],\
          5:['f4',3],6:['g4',4],7:['a4',4],8:['c4',5],9:['d4',5]}

# F# pentatonic: F#, G#, A#, C#, D#, F#
F_sharp_pent={0:['f#3',1],1:['g#3',1],2:['a#3',2],3:['c#3',2],4:['d#3',3],\
              5:['f#4',3],6:['g#4',4],7:['a#4',4],8:['c#4',5],9:['d#4',5]}


###############################################################


pi=31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
e =27182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
golden_ratio=161803398874989484820458683436563811772030917980576286213544862270526046281890\
244970720720418939113748475408807538689175212663386222353693179318006076672635\
443338908659593958290563832266131992829026788067520876689250171169620703222104\
321626954862629631361443814975870122034080588795445474924618569536486444924104\
432077134494704956584678850987433944221254487706647809158846074998871240076521\
705751797883416625624940758906970400028121042762177111777805315317141011704666\
599146697987317613560067087480710131795236894275219484353056783002287856997829\
778347845878228911097625003026961561700250464338243776486102838312683303724292


def create_wav(number,scale,name):
    '''
    creates a .wav file
    number= the number which is to be converted to music
    scale= scale to be used
    name= name of the .wav file to be saved
    '''
    number=str(number)
    elements=[]
    for element in  number:
        elements.append(int(element))
    keys=[]
    for i in range(len(elements)-1):

        number=elements[i]
        next_number=elements[i+1]
        note=scale[number][0]
        duration=scale[next_number][1]
        key=(note,duration)
        keys.append(key)
    
    keys=tuple(keys)
    pysynth.make_wav(keys, fn = name+".wav")

    
# for random scales in each iteration uncomment the following and comment the above definition 
'''
scale=[C_sharp_pent,D_sharp_pent,D_pent,E_pent,E_sharp_pent,F_pent,F_sharp_pent]

def create_wav(number,scale,name):
    '''
    creates a .wav file
    number= the number which is to be converted to music
    scale= scale list to be used of which scales would be randomly chosen 
    name= name of the .wav file to be saved
    '''
    
    number=str(number)
    elements=[]
    for element in  number:
        elements.append(int(element))
    keys=[]
    for i in range(len(elements)-1):
        scale_iter=np.random.choice(scale,len(scale))[0]
        number=elements[i]
        next_number=elements[i+1]
        note=scale_iter[number][0]
        duration=scale[next_number][1]
        key=(note,duration)
        keys.append(key)
    
    keys=tuple(keys)
    pysynth.make_wav(keys, fn = name+".wav")

'''
    
    
    
#uncomment to create the .wav file
#create_wav(pi,C_major_pent,'pi')
#create_wav(e,C_major_pent,'e')
#create_wav(golden_ratio,C_major_pent,'golden_ratio')

