import sys
def check_disk_content(file):
    try:
        number_of_disk = int(file.readline())
        rods=[[],[],[]]
        game_start=[]
        for x in range(number_of_disk):
            rods[0].append(x+1)
            game_start.append(x+1)
        return [rods,number_of_disk,game_start]
    except ValueError:
        return "NO","","" #Number of disk need to be a number,you entered char")
        
def check_moves_content(file):
        for x in file:
            try:
                x=int(x)
                source=x / 10
                dest=x % 10
                if int(source)<=NUM_OF_RODS and dest<=NUM_OF_RODS: 
                    moves.append(x)
                else:
                     return "NO" # invalid number in movent-need to be between 1 to 3
            except ValueError:
                return "NO" #Number of movements need to be a number,you entered char
        return moves  
    
def check_disk_moves(moves_loop):
    try:
        for count_moves in moves:
            moves_loop+=1
            source=int(count_moves / 10)
            dest=count_moves % 10
            if len(rods[dest-1]) == 0 or (rods[source-1][0]) < (rods[dest-1][0]): #if destination is empty
                rods[dest-1].insert(0,rods[source-1][0])
                rods[source-1].pop(0)
            else:
                return "NO"    #try to put bigger number avobe lower numbers
        if game_start==rods[len(rods)-1]:
            return "YES"#Correct solution     
        else:
            return "NO" #final situation is not like start
    except IndexError:
        return "Error"
                   
try:
    file = open(sys.argv[1])
except IndexError:
    print("Enter file name to test, python hanoy.py test(3,4,5).txt")
    exit(1)  
    
NUM_OF_RODS=3
moves = []
moves_loop=0

rods,number_of_disk,game_start=check_disk_content(file)

if rods=="NO":
    print("NO")
    exit(1)
    
moves=check_moves_content(file)
if moves=="NO":
    print("NO")
    exit(1)
result_hanoi=check_disk_moves(moves_loop)
print(result_hanoi)

