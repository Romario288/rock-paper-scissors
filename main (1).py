import random, time
comp_turn = ['k', 'n', 'b']
count = [0, 0]


def knb_choice(t):
    if t == 'k':
        print('камень')
    elif t == 'n':
        print('ножницы')
    elif t == 'b':
        print('бумага')


def main():
    gameloop = True
    while gameloop:
        turn = input('k - камень, n - ножницы, b - бумага, exit_ - выход')
        time.sleep(0.5)
        if turn == 'exit_':
            print('Выход')
            gameloop = False
        else:
            knb_choice(turn)
            c_turn = random.choice(comp_turn)
            knb_choice(c_turn)
            if (turn == 'k' and c_turn =='n') or (turn == 'n' and c_turn =='b') or (turn == 'b' and c_turn =='k'):
                print("Вы выиграли")
                count[0] += 1
            if turn == 'n' and c_turn =='k' or turn == 'b' and c_turn =='n' or turn == 'k' and c_turn =='b':
                print("Вы проиграли")
                count[1] += 1
            elif turn == 'n' and c_turn =='n' or turn == 'b' and c_turn =='b' or turn == 'k' and c_turn =='k':
                print('Ничья')
        print('Счёт - ', count[0], ':', count[1])
        if 10 in count:
            gameloop = False


if __name__ == '__main__':
    main()