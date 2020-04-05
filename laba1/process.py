
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
        if self.sms_count > 5:
            sms_count = self.sms_count - 5
            if sms_count > 10:
                return (sms_count - 5) * 2 + 5
            else:
                return self.sms_count * 1
        return 0

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