import re
import sys

from config import S_J, S_C, STATES, V_EMPTY, V_1, V_O
from exceptions import InvalidFirstCharacter, InvalidValuesInString, InvalidLine


class BarcodeDecoder:
    def __init__(self) -> None:
        self.__line:str

    def set_line(self,line:str)->None:
        pattern = "^J(J|C)*$"
        if not re.match(pattern,line):
            raise InvalidLine()

        self.__line = line

    def _comparing_previous_values(self,item:str, index:int, items:list[str], count:int)->tuple[str,int]:
        result=""
        if  item == S_C:
            count +=1
            result+=V_EMPTY
        elif item == S_J: 
            if count > 0:
                if count == 1:
                    result+=V_O
                elif count == 2:
                    result+=V_1
                else:
                    result+=V_EMPTY
                count = 0
            elif count == 0 and items[index-1]==S_J:
                result+=V_EMPTY

        return result, count

    def decode(self)->None:
        items = list(self.__line)
        if not set(items).issubset(set(STATES)):
            raise InvalidValuesInString()
        
        count = 0
        result = ""

        for index, item in enumerate(items):
            # print(item,index)
            if index == 0:
                if  item == S_C:
                    raise InvalidFirstCharacter()
                    
            elif index == 1:
                if  item == S_C:
                    count +=1
                result+=V_EMPTY
                
            else:
                r, count = self._comparing_previous_values(item, index, items, count)
                result+=r

        r, _ = self._comparing_previous_values(item, index, items, count)
        result+=r

        sys.stdout.write(result)
        # print(result)
        # print(len(result))

        # print(items)
    