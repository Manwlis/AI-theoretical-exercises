# global variables
NUM_CANNIBALS = 3
NUM_MISSIONARIES = 3

class state():
	# constructor
    def __init__( self , cannibals_left , missionaries_left , cannibals_right , missionaries_right , boat_side , action , parent ):
        self.cannibals_left = cannibals_left
        self.missionaries_left = missionaries_left
        self.cannibals_right = cannibals_right
        self.missionaries_right = missionaries_right
        self.boat_side = boat_side
        self.action = action # String pou deixnei ti egine se auto to state. Den kserw kata poso xreiazetai. Isws einai reduntand kai na mporei na ftiaxtei kata to print apo to boat side kai ta noumera self kai patera
        self.parent = parent
        self.children = list()

    # true otan lu8hke to problhma
    def is_goal_state(self):
        return ( self.cannibals_right == NUM_CANNIBALS and self.missionaries_right == NUM_MISSIONARIES )


# isws kapioi elegxoi einai reduntant
# elenxei an ena state einai egkuro
def is_valid_state( cannibals_left , missionaries_left , cannibals_right , missionaries_right ):

    #den prepei na iparxei arnhtikos ari8mos an8rwpwn h na kseperasoun ta arxika oria 
    if cannibals_left < 0 or cannibals_left > NUM_CANNIBALS:
        return False
    if missionaries_left < 0 or missionaries_left > NUM_MISSIONARIES:
        return False
    if cannibals_right < 0 or cannibals_right > NUM_CANNIBALS:
        return False
    if missionaries_right < 0 or missionaries_right > NUM_MISSIONARIES:
        return False

    # prepei na iparxoun 3 kaniballoi sunolika
    if cannibals_left + cannibals_right != NUM_CANNIBALS:
        return False
    # prepei na iparxoun 3 ierapostoloi sunolika
    if missionaries_left + missionaries_right != NUM_MISSIONARIES:
        return False

    # oi kanibaloi trwne tous ierapostolous
    if missionaries_left < cannibals_left and missionaries_left != 0:
        return False
    if missionaries_right < cannibals_right and missionaries_right != 0:
        return False

    # isws na mhn prepei na afisw ena state na einai idio me to patera tou patera tou ------------------------------

    return True


# Elenxei oles tis kiniseis an einai egkures. Gia opoies einai ftiaxnei neo state.
# pi8anes kiniseis: 
# ierapostoloi , kanibaloi , kateu8unsh
#       2      ,     0     ,     ->
#       1      ,     0     ,     ->
#       1      ,     1     ,     ->
#       0      ,     1     ,     ->
#       0      ,     2     ,     ->
#       2      ,     0     ,     <-
#       1      ,     0     ,     <-
#       1      ,     1     ,     <-
#       0      ,     1     ,     <-
#       0      ,     2     ,     <-
def create_children( parent ):
    
    # h barka einai sta aristera
    if parent.boat_side == "left":
        # 2 ierapostoloi pros ta deksia
        if is_valid_state( parent.cannibals_left , parent.missionaries_left - 2 , parent.cannibals_right , parent.missionaries_right + 2 ):
            child = state( parent.cannibals_left , parent.missionaries_left - 2 , parent.cannibals_right , parent.missionaries_right + 2, "right" , "2 missionaries to right" , parent )
            parent.children.append(child)
        # 1 ierapostolos pros ta deksia
        if is_valid_state( parent.cannibals_left , parent.missionaries_left - 1 , parent.cannibals_right , parent.missionaries_right + 1 ):
            child = state( parent.cannibals_left , parent.missionaries_left - 1 , parent.cannibals_right , parent.missionaries_right + 1, "right" , "1 missionary to right" , parent )
            parent.children.append(child)
        # 1 ierapostolos kai enas kanibalos pros ta deksia
        if is_valid_state( parent.cannibals_left - 1 , parent.missionaries_left - 1 , parent.cannibals_right + 1 , parent.missionaries_right + 1 ):
            child = state( parent.cannibals_left - 1 , parent.missionaries_left - 1 , parent.cannibals_right + 1 , parent.missionaries_right + 1, "right" , "1 missionary and 1 cannibal to right" , parent )
            parent.children.append(child)
        # 1  kanibalos pros ta deksia
        if is_valid_state( parent.cannibals_left - 1 , parent.missionaries_left , parent.cannibals_right + 1 , parent.missionaries_right ):
            child = state( parent.cannibals_left - 1 , parent.missionaries_left , parent.cannibals_right + 1 , parent.missionaries_right , "right" , "1 cannibal to right" , parent )
            parent.children.append(child)
        # 2  kanibalooi pros ta deksia
        if is_valid_state( parent.cannibals_left - 2 , parent.missionaries_left , parent.cannibals_right + 2 , parent.missionaries_right ):
            child = state( parent.cannibals_left - 2 , parent.missionaries_left , parent.cannibals_right + 2 , parent.missionaries_right , "right" , "1 cannibals to right" , parent )
            parent.children.append(child)

    # h barka einai sta deksia
    if parent.boat_side == "right":
        # 2 ierapostoloi pros ta deksia
        if is_valid_state( parent.cannibals_left , parent.missionaries_left + 2 , parent.cannibals_right , parent.missionaries_right - 2 ):
            child = state( parent.cannibals_left , parent.missionaries_left + 2 , parent.cannibals_right , parent.missionaries_right - 2 , "left" , "2 missionaries to left" , parent )
            parent.children.append(child)
        # 1 ierapostolos pros ta deksia
        if is_valid_state( parent.cannibals_left , parent.missionaries_left + 1 , parent.cannibals_right , parent.missionaries_right - 1 ):
            child = state( parent.cannibals_left , parent.missionaries_left + 1 , parent.cannibals_right , parent.missionaries_right - 1 , "left" , "1 missionary to left" , parent )
            parent.children.append(child)
        # 1 ierapostolos kai enas kanibalos pros ta deksia
        if is_valid_state( parent.cannibals_left + 1 , parent.missionaries_left + 1 , parent.cannibals_right - 1 , parent.missionaries_right - 1 ):
            child = state( parent.cannibals_left + 1 , parent.missionaries_left + 1 , parent.cannibals_right - 1 , parent.missionaries_right - 1 , "left" , "1 missionary and 1 cannibal to left" , parent )
            parent.children.append(child)
        # 1  kanibalos pros ta deksia
        if is_valid_state( parent.cannibals_left + 1 , parent.missionaries_left , parent.cannibals_right - 1 , parent.missionaries_right ):
            child = state( parent.cannibals_left + 1 , parent.missionaries_left , parent.cannibals_right - 1 , parent.missionaries_right , "left" , "1 cannibal to left" , parent )
            parent.children.append(child)
        # 2  kanibaloi pros ta deksia
        if is_valid_state( parent.cannibals_left + 2 , parent.missionaries_left , parent.cannibals_right - 2 , parent.missionaries_right ):
            child = state( parent.cannibals_left + 2 , parent.missionaries_left , parent.cannibals_right - 2 , parent.missionaries_right , "left" , "1 cannibals to left" , parent )
            parent.children.append(child)


# mallon idfs
# 8a ftiaxnei paidia mesw ths create children kai meta 8a ta psaxnei
def search_algorithm( problem ):
    return False


# prepei na ta ektupwsei afou exei bre8ei ena oloklhro monopati. Mporei na dimiourgh8oun branches pou den ftanoun sto goal. Oi katastaseis tou den prepei na ektupw8oun
def print_solution( problem ):
    return False


def main():
    # create initial state
    problem = state( NUM_CANNIBALS , NUM_MISSIONARIES , 0 , 0 , "left" , "no action" , None )
    create_children( problem )

    print( problem.children )

    # find solution
    search_algorithm( problem )

    # print solution
    print_solution( problem )
    

# # na koitaksw an xreiazetai na meinei
if __name__ == "__main__":
    main()