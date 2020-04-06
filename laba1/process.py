
TARGET_PHONE = "915642913"

class Biller(object):
    def __init__(self):
        self.incoming_calls = 0.0
        self.outcoming_calls = 0.0
        self.sms_count = 0

    def add_new(self, time, src, dst, duration, sms_count):
        if src == TARGET_PHONE:
            self.incoming_calls += float(duration)
            self.sms_count += int(sms_count)
            return

        if dst == TARGET_PHONE:
            self.outcoming_calls += float(duration)

    def get_cost_call(self):
        return self.incoming_calls + self.outcoming_calls

    def get_cost_sms(self):
        cost = 0
        
        if self.sms_count > 5:
            cost += min(self.sms_count - 5, 5)
        
        if self.sms_count > 10:
            cost += (self.sms_count - 10) * 2

        return cost

    def get_cost(self):
        return self.get_cost_call() + self.get_cost_sms()


def main():
    with open("data.csv", "r") as file:
        for line in file:
            break
        
        biller = Biller()

        for line in file:
            biller.add_new(*line.split(","))
        
        print("Bill for calls:", biller.get_cost_call())
        print("Bill for SMS:", biller.get_cost_sms())
        print("Total bill:", biller.get_cost())


if __name__ == "__main__":
    main()