from typing import Iterable
import random
random.seed()


class Bush:
    """bush with berries or maybe not :D"""
    def __init__(self,r):
        self.berries=random.randint(0,15)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.berries})'

    def getBerries(self):
        return self.berries


def crawler(bushes):
    total='\n'.join([f'№{i} - {b}' for i,b in enumerate(bushes, start=0)])
    print(f"Bushes:\n{total}")
    chunks=[]
    if len(bushes) > 3 and not all([isinstance(inst,Bush) for inst in bushes]):
        raise ValueError('wrong bush grade')
    if len(bushes) < 3:
        raise ValueError('garden is too small')
    elif len(bushes) > 2147483647:
        raise ValueError('garden is too big')

    for i,b in enumerate(bushes, start=0):
        prev = len(bushes)-1 if i == 0 else i - 1
        next = 0 if i == len(bushes)-1 else  i + 1
        multibush=sum([bushes[i].getBerries() for i in (prev,i,next)])
        chunks.append({'midbush':i,'berries':multibush})

    return max(chunks, key=lambda tribush:tribush['berries'])


if __name__=='__main__':
    bushes=[Bush(i) for i in range(10)]
    max=crawler(bushes)
    print(max)
