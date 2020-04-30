"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.
        """
        Thread.__init__(self)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.kwargs = kwargs

        """"
        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
    def run(self):
        for cart in self.carts:
            cart_id = self.marketplace.new_cart()
            for elem in cart:
                for iteration in range(elem["quantity"]):
                    if elem["type"] == "add":
                        tmp = self.marketplace.add_to_cart(cart_id, elem["product"])
                        while tmp is False:
                            time.sleep(self.retry_wait_time)
                            tmp = self.marketplace.add_to_cart(cart_id, elem["product"])
                    if elem["type"] == "remove":
                        self.marketplace.remove_from_cart(cart_id, elem["product"])
                    _ = iteration

            my_list = self.marketplace.place_order(cart_id)
            for prod in my_list:
                print("%s bought %s" % (self.kwargs['name'], prod))
