import asyncio
import random
import time
from datetime import datetime

# 4.1
async def get_camera_data(camera_id):
    delay = random.uniform(0.1, 5)
    await asyncio.sleep(delay + 0.5)
    return {
        "camera_id": camera_id,
        "timestamp": datetime.now().isoformat(),
        "vehicle_count": random.randint(5, 20)
    }

# 4.2
async def main():
    start = time.time()
    ciklusi = 0
    statistika = {i: [] for i in range(1, 6)}
    
    while time.time() - start < 30:
        cycle_start = time.time()
        ciklusi += 1
        print(f"\nCiklus {ciklusi}")
        
        tasks = []
        for i in range(1, 6):
            # 4.3 Timeout
            tasks.append(asyncio.wait_for(get_camera_data(i), timeout=3.0))
            
        rezultati = await asyncio.gather(*tasks, return_exceptions=True)
        
        validni = []
        for i, res in enumerate(rezultati):
            cid = i + 1
            if isinstance(res, asyncio.TimeoutError):
                print(f"Upozorenje: Dohvat podataka s kamere {cid} je istekao.")
            elif not isinstance(res, Exception):
                validni.append(res)
                statistika[cid].append(res["vehicle_count"])

        if validni:
            validni.sort(key=lambda x: datetime.fromisoformat(x["timestamp"]))
            print(f"Prva: {validni[0]['camera_id']}, Zadnja: {validni[-1]['camera_id']}")
            print(f"Ukupno: {sum(v['vehicle_count'] for v in validni)}")
        
        elapsed = time.time() - cycle_start
        if elapsed < 5:
            await asyncio.sleep(5 - elapsed)

    print("\n--- Prosjek ---")
    for cid, vals in statistika.items():
        avg = sum(vals) / len(vals) if vals else 0
        print(f"Kamera {cid}: {avg:.2f}")

if __name__ == "__main__":
    asyncio.run(main())