import sys
import random
import re

from card import card

suits = {"spade": 0, "heart": 1, "club": 2, "diamond": 3}    # transfer suit into suit ID
types = {0: "high card", 1: "a pair", 2: "two pairs", 3: "three of a kind", 4: "straight", 5: "flush", 6: "full house",
         7: "four of a kind", 8: "flush straight"}


def check_input(input1, input2=""):
    """
    :param input1: string
    :param input2: string
    :return:
    """
    if not re.match(r'[0-3] [0-9]+ [0-3] [0-9]+', input1):
        sys.stderr.write("Error: wrong input of P1\n")
        return False
    if input2:
        if not re.match(r'[0-3] [0-9]+ [0-3] [0-9]+', input2):
            sys.stderr.write("Error: wrong input of P2\n")
            return False
    handpool = []
    p1numbers = input1.split(" ")
    if int(p1numbers[1]) > 13 or int(p1numbers[3]) > 13:
        sys.stderr.write("Error: No such card\n")
        return False
    handpool.append((p1numbers[0], p1numbers[1]))
    handpool.append((p1numbers[2], p1numbers[3]))
    if len(set(handpool)) < 2:
        sys.stderr.write("Error: Duplicate card in P1 hand\n")
        return False
    if input2:
        p2numbers = input2.split(" ")
        if int(p2numbers[1]) > 13 or int(p2numbers[3]) > 13:
            sys.stderr.write("Error: No such card\n")
            return False
        handpool.append((p2numbers[0], p2numbers[1]))
        handpool.append((p2numbers[2], p2numbers[3]))
        if len(set(handpool)) < 4:
            sys.stderr.write("Error: Duplicate card\n")
            return False
    return True


def check_hands(cards):
    '''
    judge the type of the hand and return the type name and the highest number of the cards
    :param cards: List(card)
    :return: (type, highest card)
    '''

    def check_flush(cards):
        '''
        check the if cards is flush
        :param cards: List(int)
        :return: Bool
        '''
        suit_temp = cards[0].suit
        for card_inner in cards:
            if card_inner.suit != suit_temp:
                return False
        return True

    def check_staight(card_numbers):
        '''
        check if the cards is straight
        :param card_numbers: List(int)
        :return: Bool
        '''
        if card_numbers == [1, 10, 11, 12, 13]:
            return True
        return card_numbers[-1] - card_numbers[0] == 4 and len(set(card_numbers)) == 5

    def check_four_of_a_kind(card_numbers):
        '''
        check if the cards is four of a kind
        :param card_numbers: List(int)
        :return: Bool
        '''
        if len(set(card_numbers[:-1])) == 1 or len(set(card_numbers[1:])) == 1:
            return True
        else:
            return False

    def check_full_house(card_numbers):
        '''
        check if the cards is full house
        :param card_numbers:List(int)
        :return:Bool
        '''
        if len(set(card_numbers[:3])) == 1 and len(set(card_numbers[3:])) == 1:
            return True
        elif len(set(card_numbers[:2])) == 1 and len(set(card_numbers[2:])) == 1:
            return True
        else:
            return False

    def check_three_of_a_kind(card_numbers):
        '''
        check if the cards is three a kind
        :param card_numbers: List(int)
        :return: [bool, int]
        '''
        for i in card_numbers:
            if card_numbers.count(i) == 3:
                return [True, i]
        return [False, 0]

    def check_two_pair(card_numbers):
        '''
        check if the cards is two pairs, caution: only use after three_of a kind
        :param card_numbers: List(int)
        :return: bool
        '''
        return len(set(card_numbers)) == 3

    def check_one_pair(card_numbers):
        '''
        check if the cards is one pair
        :param card_numbers: List(int)
        :return: bool
        '''
        return len(set(card_numbers)) == 4


    card_numbers = []
    for card_inner in cards:
        card_numbers.append(int(card_inner.point))
    card_numbers.sort()

    # check the flush straight
    if check_flush(cards) and check_staight(card_numbers):
        if card_numbers[0] != 1:
            return [8, card_numbers[0]]
        else:
            if card_numbers[1] == 10:
                return [8, 10]
            else:
                return [8, 1]

    # check the four of a kind
    if check_four_of_a_kind(card_numbers):
        if card_numbers.count(card_numbers[0]) == 4:
            return [7, card_numbers[0]]
        else:
            return [7, card_numbers[-1]]

    # check the full house
    if check_full_house(card_numbers):
        if card_numbers.count(card_numbers[0]) == 3:
            return [6, card_numbers[0]]
        else:
            return [6, card_numbers[-1]]

    # check flush
    if check_flush(cards):
        return [5, card_numbers[-1]]

    # check straight
    if check_staight(card_numbers):
        if card_numbers[0] != 1:
            return [4, card_numbers[0]]
        else:
            if card_numbers[1] == 10:
                return [4, 10]
            else:
                return [4, 1]

    # check three of a kind
    result = check_three_of_a_kind(card_numbers)
    if result[0]:
        return [3, result[1]]

    # check two pair
    if check_two_pair(card_numbers):
        return [2, card_numbers[-2]]

    # check one pair
    if check_one_pair(card_numbers):
        for i in card_numbers:
            if card_numbers.count(i) == 2:
                return [1, i]

    # high card
    if card_numbers[0] == 1:
        return [0, card_numbers[0]]
    else:
        return [0, card_numbers[-1]]


def if_p1_win(p1, p2):
    '''

    :param p1: List(card)
    :param p2: List(card)
    :return: 0:p1<p2, 1:p1>p2, 2:p1=p2
    '''
    p1_result = check_hands(p1)
    p2_result = check_hands(p2)
    if p1_result[1] == 1 and p1_result[0] != 4 and p1_result[0] != 8:
        p1_result[1] = 14
    if p2_result[1] == 1 and p2_result[0] != 4 and p2_result[0] != 8:
        p2_result[1] = 14
    if p1_result[0] < p2_result[0]:
        return 0
    elif p1_result[0] > p2_result[0]:
        return 1
    else:
        if p1_result[1] < p2_result[1]:
            return 0
        elif p1_result[1] > p2_result[1]:
            return 1
        else:
            # if the highest card an the type are all the same, compare the two cards one by one to find a winner
            for i in range(4, -1, -1):
                if p1[i].point < p2[i].point:
                    return 0
                elif p1[i].point > p2[i].point:
                    return 1
            return 2


def random_pick(A0, A1, B0, B1):
    '''
    random pick 10000 hands card and calculate the win rate
    :param A0: card - P1 first
    :param A1: card - P1 second
    :param B0: card - P2 first
    :param B1: card - P2 second
    :return: None
    '''
    p1_win_times = 0
    p2_win_times = 0
    draw_times = 0

    for j in range(1000):

        tables = []
        all_cards = [A0, A1, B0, B1]

        # table_output = "The cards on table: "
        while len(tables) != 5:
            newcard = card(0, 0, random.randint(0, 51))
            if newcard not in all_cards:
                tables.append(newcard)
                # table_output += str(newcard) + " "
                all_cards.append(newcard)
        # print(table_output)

        P1_final = tables[:]

        for i in range(6):
            for j in range(i + 1, 7):
                temp = tables[:] + [A0, A1]
                del temp[j]
                del temp[i]
                if if_p1_win(P1_final, temp) == 0:
                    P1_final = temp[:]

        P2_final = tables[:]

        for i in range(6):
            for j in range(i + 1, 7):
                temp = tables[:] + [B0, B1]
                del temp[j]
                del temp[i]
                if if_p1_win(P2_final, temp) == 0:
                    P2_final = temp[:]

        # #  the output of the two results
        # p1_output = "p1: "
        # for ca in P1_final:
        #     p1_output += str(ca) + " "
        # print(p1_output)
        # result = check_hands(P1_final)
        # print("the type is " + types[result[0]] + ", and the index of it is " + str(result[1]))
        #
        # p2_output = "p2: "
        # for ca in P2_final:
        #     p2_output += str(ca) + " "
        # print(p2_output)
        # result = check_hands(P2_final)
        # print("the type is " + types[result[0]] + ", and the index of it is " + str(result[1]))

        if if_p1_win(P1_final, P2_final) == 1:
            # print("P1 wins")
            p1_win_times += 1
        elif if_p1_win(P1_final, P2_final) == 0:
            # print("P2 wins")
            p2_win_times += 1
        else:
            # print("draw")
            draw_times += 1
        # print("-----------------------------")
    print("P1 win rate: " + str(p1_win_times / 10) + "%")
    print("P2 win rate: " + str(p2_win_times / 10) + "%")
    print("Draw rate  : " + str(draw_times / 10) + "%")

def test_case_random_pick():
    '''
    random pick 10000 hands card and calculate the win rate
    :param A0: card - P1 first
    :param A1: card - P1 second
    :param B0: card - P2 first
    :param B1: card - P2 second
    :return: None
    '''
    p1_win_times = 0
    p2_win_times = 0
    draw_times = 0
    A0 = card(0,2)
    A1 = card(1,7)
    count = 0
    while count < 10000:

        B0 = card(random.randint(0,3),random.randint(1,13))
        B1 = card(random.randint(0,3),random.randint(1,13))
        #B0 = card(0,13)
        #B1 = card(1,13)
        all_cards = [A0,A1]
        if B0 in all_cards or B1 in all_cards or B0.index == B1.index:
            continue
        tables = []
        all_cards.append(B0)
        all_cards.append(B1)
        # print("P1: " + str(A0) + " " + str(A1))
        # print("P2: " + str(B0) + " "+str(B1))
        # table_output = "The cards on table: "
        while len(tables) != 5:
            newcard = card(0, 0, random.randint(0, 51))
            if newcard not in all_cards:
                tables.append(newcard)
                # table_output += str(newcard) + " "
                all_cards.append(newcard)
        # print(table_output)

        P1_final = tables[:]

        for i in range(6):
            for j in range(i + 1, 7):
                temp = tables[:] + [A0, A1]
                del temp[j]
                del temp[i]
                if if_p1_win(P1_final, temp) == 0:
                    P1_final = temp[:]

        P2_final = tables[:]

        for i in range(6):
            for j in range(i + 1, 7):
                temp = tables[:] + [B0, B1]
                del temp[j]
                del temp[i]
                if if_p1_win(P2_final, temp) == 0:
                    P2_final = temp[:]

        # #  the output of the two results
        # p1_output = "p1: "
        # for ca in P1_final:
        #     p1_output += str(ca) + " "
        # print(p1_output)
        # result = check_hands(P1_final)
        # print("the type is " + types[result[0]] + ", and the index of it is " + str(result[1]))
        #
        # p2_output = "p2: "
        # for ca in P2_final:
        #     p2_output += str(ca) + " "
        # print(p2_output)
        # result = check_hands(P2_final)
        # print("the type is " + types[result[0]] + ", and the index of it is " + str(result[1]))

        if if_p1_win(P1_final, P2_final) == 1:
            # print("P1 wins")
            p1_win_times += 1
        elif if_p1_win(P1_final, P2_final) == 0:
            # print("P2 wins")
            p2_win_times += 1
        else:
            # print("draw")
            draw_times += 1
        # print("-----------------------------")
        count+=1
    print("P1 win rate: " + str(p1_win_times / 100) + "%")
    print("P2 win rate: " + str(p2_win_times / 100) + "%")
    print("Draw rate  : " + str(draw_times / 100) + "%")


def bruce_pick(A0, A1, B0, B1):
    '''
    bruce pick all the possible card and calculate the win rate
    :param A0: card - P1 first
    :param A1: card - P1 second
    :param B0: card - P2 first
    :param B1: card - P2 second
    :return: None
    '''
    p1_win_times = 0
    p2_win_times = 0
    draw_times = 0
    count = 0

    tables = []
    all_cards = [A0, A1, B0, B1]
    cards_left = list(range(52))
    for number in all_cards:
        cards_left.remove(number.index)
    for k1 in range(44):
        for k2 in range(k1+1, 45):
            for k3 in range(k2+1, 46):
                for k4 in range(k3+1, 47):
                    for k5 in range(k4+1, 48):
                        count += 1

                        tables.append(card(0, 0, k1))
                        tables.append(card(0, 0, k2))
                        tables.append(card(0, 0, k3))
                        tables.append(card(0, 0, k4))
                        tables.append(card(0, 0, k5))

                        P1_final = tables[:]

                        for i in range(6):
                            for j in range(i + 1, 7):
                                temp = tables[:] + [A0, A1]
                                del temp[j]
                                del temp[i]
                                if if_p1_win(P1_final, temp) == 0:
                                    P1_final = temp[:]

                        P2_final = tables[:]

                        for i in range(6):
                            for j in range(i + 1, 7):
                                temp = tables[:] + [B0, B1]
                                del temp[j]
                                del temp[i]
                                if if_p1_win(P2_final, temp) == 0:
                                    P2_final = temp[:]
                        if if_p1_win(P1_final, P2_final) == 1:
                            p1_win_times += 1
                        elif if_p1_win(P1_final, P2_final) == 0:
                            p2_win_times += 1
                        else:
                            draw_times += 1

    print("P1 win rate: " + str(p1_win_times / count) + "%")
    print("P2 win rate: " + str(p2_win_times / count) + "%")
    print("Draw rate  : " + str(draw_times / count) + "%")




def main():
    # while True:
    #     first_hand = input("Input the first hand:")
    #     if first_hand == ' ':
    #         break
    #     if not check_input(first_hand):
    #         continue
    #
    #     second_hand = input("Input the second hand:")
    #     if second_hand == ' ':
    #         break
    #     if not check_input(first_hand, second_hand):
    #         continue
    #
    #     first_hand = first_hand.split(" ")
    #     A0 = card(int(first_hand[0]), int(first_hand[1]))
    #     A1 = card(int(first_hand[2]), int(first_hand[3]))
    #
    #     second_hand = second_hand.split(" ")
    #     B0 = card(int(second_hand[0]), int(second_hand[1]))
    #     B1 = card(int(second_hand[2]), int(second_hand[3]))
    #     print("P1: " + str(A0) + " "+str(A1))
    #     print("P2: " + str(B0) + " "+str(B1))
    #
    #     random_pick(A0, A1, B0, B1)
        # bruce_pick(A0, A1, B0, B1)

    test_case_random_pick()


    sys.exit(0)


if __name__ == '__main__':
    main()

