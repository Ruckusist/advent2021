# start with some imports
import os, sys, asyncio
import time, datetime
from timeit import default_timer as timer

# and the utils
def open_day(day=1):
    return [x.strip() for x in open(f"data/day{day}.txt", "r").readlines()]

def make_data(data):
    return [int(x) for x in data[0].split(',')]

async def do_one(number):
    print(f"doing number {number}")
    new_data = []
    if not number:  # if 0 then spawn a new fish
        new_data.append(6)
        new_data.append(8)
    else:
        new_data.append(number-1)
    return new_data

def update(data): pass

async def main():
    raw_data = open_day(6)
    data = make_data('3,4,3,1,2')
    data.extend(await asyncio.wait_for(
        asyncio.gather(
        *[do_one(x) for x in data]
    ), timeout=10.0))
    print(data)

if __name__ == "__main__":
    asyncio.run(main())