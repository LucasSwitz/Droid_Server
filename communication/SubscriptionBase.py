from enum import Enum
import abc


class SubscriptionBase:
    def __init__(self):
        print("Created SubscriptionBase")
        self._subscriptions = dict()

    def add_subscriber(self, subscriber):

        for subscription in subscriber.subscriptions:
            if subscription.get_name not in self._subscriptions:
                self._subscriptions.update(subscription.get_name, list())
            self._subscriptions.get(subscription.get_name()).append(subscriber)

    def update(self, value):
        self.update_subscribers(value)

    def update_subscribers(self, value):
        for sub in self._subscriptions.get(value.name):
            sub.on_update(value)


class Subscriber():
    def __init__(self):
        pass

    @abc.abstractmethod
    def on_update(self, value):
        """Define what to do with a value when a susbcribed value is updated"""
        return


class SubscriptionValue:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def __setattr__(self, key, value):
        self.value = value
        SubscriptionBase.update(self)


class SubscriptionType(Enum):
    BOOL = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    BYTE = 5
