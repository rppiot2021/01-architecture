from hat.drivers import iec104
import asyncio
import random
import sys


async def async_main():
    connections = set()

    currents = [1, 3, 2]

    server = await iec104.listen(
        connection_cb=connections.add,
        addr=iec104.Address('127.0.0.1', 9999))

    while server.is_open:

        await asyncio.sleep(1)

        current_selection = random.randint(0, 2)
        new_current = round(random.random() * 5, 2)
        print('changing current', current_selection, 'from',
              currents[current_selection], 'to', new_current)
        print('state:', currents)
        currents[current_selection] = new_current

        for conn in connections:
            if conn.is_open:
                conn.notify_data_change([iec104.Data(
                    asdu_address=current_selection,
                    io_address=0,
                    cause=iec104.Cause.SPONTANEOUS,
                    is_test=False,
                    quality=iec104.Quality(blocked=False,
                                           invalid=False,
                                           not_topical=False,
                                           overflow=False,
                                           substituted=False),
                    time=None,
                    value=iec104.FloatingValue(new_current))])


def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    sys.exit(main())
