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
        self.children = list() # isws den xreiazetai na einai edw kai na einai temp sth dfs

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

    parent.children = list()

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
            child = state( parent.cannibals_left - 2 , parent.missionaries_left , parent.cannibals_right + 2 , parent.missionaries_right , "right" , "1 cannibal to right" , parent )
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
            child = state( parent.cannibals_left + 2 , parent.missionaries_left , parent.cannibals_right - 2 , parent.missionaries_right , "left" , "1 cannibal to left" , parent )
            parent.children.append(child)


# iterative deepeining depth first search
def id_dfs( root ):
    import itertools

    # ftiaxnei paidia mesw ths create children kai meta 8a ta psaxnei
    def dfs( node , depth_remaining ):
        # eftase sto orio ba8ous
        if depth_remaining == 0:
            return None
        # brhke stoxo
        elif node.is_goal_state():
            return node

        # ftiaxnei paidia
        create_children( node )

        # stelnei ta paidia gia psaksimo anadromika
        for child in node.children:
            result = dfs(child, depth_remaining - 1)
            # paidi tou eftase se stoxo
            if result:
                return result
        # ola ta paidia ftasan se adieksodo h pato
        return None

    # infinite counter
    for depth in itertools.count():
        route = dfs( root , depth )
        if route:
            return route


# prepei na ta ektupwsei afou exei bre8ei ena oloklhro monopati. Mporei na dimiourgh8oun branches pou den ftanoun sto goal. Oi katastaseis tous den prepei na ektupw8oun
def print_solution( solution ):

    path = list()

    # kataskeuh monopatiou
    while solution:
        path.append(solution)
        solution = solution.parent

    print("")
    # ektupwsh kinisewn. Sto initial state den exei geinei kamia kinhsh
    for i in range( 1 , len(path) ):
        # exoun mpei sth lista apo goal pros arxh. Prepei na bgoun anapoda gia na emfanistoun swsta
        state = path[ len(path) - i - 1 ]
        print( f"action {i:>2}: {state.action}" )

    print("")
    # ektupwsh katastasewn
    for i in range( 0 , len(path) ):
        state = path[ len(path) - i - 1 ]
        if i == 0:
            print( f"init state: {NUM_CANNIBALS}C {NUM_MISSIONARIES}M left  0C 0M" )
        elif i != len(path) - 1:
            print( f" state  {i:>2}: {state.cannibals_left}C {state.missionaries_left}M {state.boat_side:<5} {state.cannibals_right}C {state.missionaries_right}M" )
        else:
            print( f" end state: {state.cannibals_left}C {state.missionaries_left}M {state.boat_side:<5} {state.cannibals_right}C {state.missionaries_right}M" )


def main():
    # create initial state
    problem = state( NUM_CANNIBALS , NUM_MISSIONARIES , 0 , 0 , "left" , "" , None )

    # find solution
    solution = id_dfs( problem )

    # print solution
    print_solution( solution )


# run from terminal
if __name__ == "__main__":
    main()