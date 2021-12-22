import sys

from config import S_J, S_C, V_EMPTY, V_1, V_O


class BarcodeDecoder:
    def __init__(self) -> None:
        self.__count=0
        self.__state = V_EMPTY
        self.__previous_state = None

    def set_state_up(self):
        if self.__count == 2:
            self.__state = V_O
        elif self.__count == 3:
            self.__state = V_1
        else:
            self.__state =V_EMPTY

    def decode(self, c:str)->None:
        if c == S_J:
            if self.__count == 0:
                self.__count+=1
                sys.stdout.write(V_EMPTY)
            else:
                self.__count = 1
                if self.__previous_state == S_J:
                    sys.stdout.write(V_EMPTY)
                elif self.__previous_state == S_C:
                    sys.stdout.write(self.__state)

            self.__previous_state =S_J

        elif c == S_C:
            sys.stdout.write(V_EMPTY)
            if self.__count > 0:
                self.__count+=1
                self.set_state_up()
            self.__previous_state =S_C
