import time
import asyncio
import requests
import aiohttp

# 3.1
def zadatak(sekunde):
    time.sleep(sekunde)
    return f"zadatak završen nakon {sekunde} sekundi."

# 3.2
async def asinkroni_zadatak(sekunde):
    await asyncio.sleep(sekunde)
    return f"zadatak završen nakon {sekunde} sekundi."

# 3.3
def posalji_zahtjev(url):
    return requests.get(url).json()

# 3.4
async def asinkroni_posalji_zahtjev(url, session): # Dodao sam session kao argument kao on
    async with session.get(url) as response:
        return await response.json()

async def main():
    # Sinkrono
    t1 = time.perf_counter() # Promjena
    zadatak(3); zadatak(2); zadatak(1)
    t2 = time.perf_counter() # Promjena
    print(f"Sync vrijeme: {t2 - t1:.2f}")

    # Asinkrono
    t1 = time.perf_counter() # Promjena
    await asyncio.gather(asinkroni_zadatak(3), asinkroni_zadatak(2), asinkroni_zadatak(1))
    t2 = time.perf_counter() # Promjena
    print(f"Async vrijeme: {t2 - t1:.2f}")

    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    # HTTP Sync
    t1 = time.perf_counter() # Promjena
    print([posalji_zahtjev(url)["title"] for _ in range(3)])
    t2 = time.perf_counter() # Promjena
    print(f"HTTP Sync: {t2 - t1:.2f}")

    # HTTP Async
    t1 = time.perf_counter() # Promjena
    async with aiohttp.ClientSession() as session: # Session otvaramo ovdje kao on
        tasks = [asinkroni_posalji_zahtjev(url, session) for _ in range(3)]
        res = await asyncio.gather(*tasks)
        print([r["title"] for r in res])
    
    t2 = time.perf_counter() # Promjena
    print(f"HTTP Async: {t2 - t1:.2f}")

if __name__ == "__main__":
    asyncio.run(main())