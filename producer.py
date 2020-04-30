"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time

class Producer(Thread):
    """
    Class that represents a producer.
    """
    producer_id = -1
    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.
        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time
        self.kwargs = kwargs

    def run(self):
        i = 0
        self.producer_id = self.marketplace.register_producer()
        while True:
            aux = self.products[i][1]
            for iteration in range(aux):
                tmp = self.marketplace.publish(self.producer_id, self.products[i][0])
                while tmp is False:
                    time.sleep(self.republish_wait_time)
                    tmp = self.marketplace.publish(self.producer_id, self.products[i][0])
                time.sleep(self.products[i][2])
                _ = iteration
            i += 1
            i %= len(self.products)
            