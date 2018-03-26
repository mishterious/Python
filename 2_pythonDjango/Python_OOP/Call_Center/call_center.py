class Call_Class(object):
    def __init__(self, id, name, phone_number, call_time, call_reason):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.call_time = call_time
        self.call_reason = call_reason

    def display(self):
        print "Here's the problem"
        print " {} {} {} {} {} ".format(self.id, self.name, self.phone_number, self.call_time, self.call_reason)
        return self


class Call_Center(object):
    def __init__(self, calls, name, call_reason, queue_size):
        self.calls = calls
        self.name = name
        self.call_reason = call_reason
        self.queue_size = []
    
    def add(self, calls):
        self.calls.append(self_calls)

    def remove(self):
        self.calls.pop(0)

    def info(self):
        print "{} {}".format(self.name, self.phone_number)

myself = Call_Class(0, "Mish", "408-839-1111", 12, "I want to make it happen")
myself.display()

