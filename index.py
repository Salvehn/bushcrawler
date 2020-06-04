from typing import Iterable

class Bush:
    """bush with berries or maybe not :D"""
    def __init__(self,r):
        self.berries=int(r)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.berries})'

    def getBerries(self):
        return self.berries


def crawler(inputstr):
    if len(inputstr) < 1:
        raise ValueError('input str too short')

    berries=inputstr.split(' ')

    if not all(i.isdigit() for i in berries):
        raise ValueError('incorrect user input')
    bushes=[Bush(i) for i in berries]

    total='\n'.join([f'№{i} - {b}' for i,b in enumerate(bushes, start=0)])
    print(f"Bushes:\n{total}")
    chunks=[]
    if len(bushes) < 3:
        raise ValueError('garden is too small')
    elif len(bushes) > 999:
        raise ValueError('garden is too big')

    for i,b in enumerate(bushes, start=0):
        prev = len(bushes)-1 if i == 0 else i - 1
        next = 0 if i == len(bushes)-1 else  i + 1
        multibush=sum([bushes[i].getBerries() for i in (prev,i,next)])
        chunks.append(i)

    return max(chunks)


if __name__=='__main__':

    max=crawler(input("Enter bushes : "))
    print('MAX berries count bush id is: ',max)
