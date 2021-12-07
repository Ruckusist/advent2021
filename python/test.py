import asyncio
from timeit import default_timer as timer

def open_day(day=1):
    return [x.strip() for x in open(f"data/day{day}.txt", "r").readlines()]

async def do_it(n):
    new_data = []
    if not n:  # if 0 then spawn a new fish
        new_data.append(6)
        new_data.append(8)
    else:
        new_data.append(n-1)
    return new_data

async def main():
    raw_data = open_day(6)
    faux_data = ['3,4,3,1,2']
    data = [int(x) for x in raw_data[0].split(',')]
    for day in range(257):
        tasks = [do_it(x) for x in data]
        dataset = []
        for future in asyncio.as_completed(tasks):
            dataset.extend( await future )
        print(f'After {day} days: {len(data)} fish')
        data = dataset


asyncio.run(main())