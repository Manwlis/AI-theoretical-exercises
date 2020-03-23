NUM_CANNIBALS = 3
NUM_MISSIONARIES = 3

def test():
    cannibals_left = 2
    missionaries_left = 3
    cannibals_right = 1
    missionaries_right = 0

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

    # isws na mhn prepei na afisw ena state na einai idiome to patera tou patera tou

    return True

print ( test() )