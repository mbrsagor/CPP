import asyncio


async def download():
    for i in range(0, 11):
        await asyncio.sleep(1)
        print(f"Download {i}% done")
    print("Thanks Sagor! Your download has been completed.")


asyncio.run(download())
