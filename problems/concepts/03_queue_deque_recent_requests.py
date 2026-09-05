"""Queue / deque practice: Count recent requests.

Problem
Requests arrive with increasing timestamps. For each new request t, keep only
requests in the last 3000 milliseconds and return the current count.

Feynman idea
A queue is a waiting line. Old requests leave from the front; new requests
join at the back.

Time: O(n) total for n requests
Space: O(n)
"""

from collections import deque


class RecentCounter:
    def __init__(self) -> None:
        self.queue: deque[int] = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)


if __name__ == "__main__":
    counter = RecentCounter()
    assert counter.ping(1) == 1
    assert counter.ping(100) == 2
    assert counter.ping(3001) == 3
    assert counter.ping(3002) == 3
    print("ok")
