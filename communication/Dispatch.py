


class Dispatch:

    class __Dispatch:
        instance = None

        def __init__(self):
            self.values = dict()
            self.subscribers = dict()

        def add_subscriber(self,key,subscriber):

            sub_list = self.subscribers.get(key)

            if sub_list is None:
                self.subscribers.update(key,list())

            self.subscribers.get(key)

        def post(self,name,value):
            self.values.update(name,value)

        def update_listeners(self,name):
            for listener in self.listeners:
                listener.update_value((name,self.values.get(name)))

    def __init__(self, arg):
        if not Dispatch.instance:
            Dispatch.instance = Dispatch.__Dispatch()

    def __getattr__(self, name):
        return getattr(self.instance, name)