import asyncio


async def main():
    # Engine
    loop = asyncio.get_running_loop()

    # Create UDP Sender
    transport, protocol = await loop.create_datagram_endpoint(
        asyncio.DatagramProtocol, remote_addr=("127.0.0.1", 9999)
    )

    message = "Hello UDP!!"
    transport.sendto(message.encode())

    print("Sent!!")
    transport.close()


asyncio.run(main())
