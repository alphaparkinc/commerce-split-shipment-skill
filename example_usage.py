from client import SplitShipmentClient
def main():
    c = SplitShipmentClient()
    print(c.plan_delivery([{"sku": "phone"}, {"sku": "case"}], {"Whse_A": ["phone"], "Whse_B": ["case"]}))
if __name__ == '__main__':
    main()
