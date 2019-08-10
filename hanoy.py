def check_disk_content(file):
    try:
        number_of_disk = int(file.readline())
        rods=[[],[],[]]
        game_start=[]
        for x in range(number_of_disk):
            rods[0].append(x+1)
            game_start.append(x+1)
        return rods,number_of_disk,game_start
    except ValueError:
        print("NO,Number of disk need to be a number,you entered char")    
        exit(1)
        
def check_moves_content(file):
        for x in file:
            try:
                x=int(x)
                source=x / 10
                dest=x % 10
                if int(source)<=NUM_OF_RODS and dest<=NUM_OF_RODS: 
                    moves.append(x)
                else:
                     print ("NO,invalid number in movent-need to be between 1 to "+ str(NUM_OF_RODS))
                     exit(1)
            except ValueError:
                print("NO,Number of movements need to be a number,you entered char")
                exit(1)      
        return moves  
    
def check_disk_moves(moves_loop):
        for count_moves in moves:
            moves_loop+=1
            source=int(count_moves / 10)
            dest=count_moves % 10
            if len(rods[dest-1]) == 0 or (rods[source-1][0]) < (rods[dest-1][0]): #if destination is empty
                rods[dest-1].insert(0,rods[source-1][0])
                rods[source-1].pop(0)
            else:
                print("NO,you try to put a big disk avobe little one")    #try to put bigger number avobe lower numbers
                exit(1)
        if game_start==rods[len(rods)-1]:
            print("YES,you did it")     
        else:
            print("NO,You missed,weong solution of Hanoi") #final situation is not like start
            exit(1)
                   
    
file = open("test5.txt")
NUM_OF_RODS=3
moves = []
moves_loop=0


rods,number_of_disk,game_start=check_disk_content(file)
moves=check_moves_content(file)
check_disk_moves(moves_loop)

