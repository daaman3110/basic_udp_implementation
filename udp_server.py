import asyncio


class UDPEcho(asyncio.DatagramProtocol):
    def datagram_received(self, data, addr):
        print(f"Received: {data.decode()} from {addr}")


async def main():
    # Engine
    loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UDPEcho(), local_addr=("0.0.0.0", 9999)
    )

    print("UDP server listening....")
    await asyncio.sleep(3600)


asyncio.run(main())
