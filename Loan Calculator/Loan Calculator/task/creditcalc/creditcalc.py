import math
import argparse


def find_problems(parsed_arg):
    availableArgs = ["diff", "annuity"]

    if parsed_arg[0] is None or parsed_arg[0] not in availableArgs:
        print("Incorrect parameters")
        return True

    if parsed_arg[0] == "diff" and parsed_arg[4] is not None:
        print("Incorrect parameters")
        return True

    counter = 0
    for i in parsed_arg:

        if i is not None and i.isdigit() and i[0] == "-":
            print("Incorrect parameters")
            return True

        if i is None:
            counter += 1

    if counter > 1:
        print("Incorrect parameters")
        return True

    return False


def calculate(parsed_arg):
    if parsed_arg[0] == "diff":
        int_principal = int(parsed_arg[1])
        int_periods = int(parsed_arg[2])
        float_interest = float(parsed_arg[3])
        differenceList = []
        for i in range(1, int_periods + 1):
            interest = float_interest / (12 * 100)
            payment = math.ceil((int_principal / int_periods) + interest * \
                                (int_principal - (int_principal * (i - 1)) / int_periods))
            differenceList.append(payment)
            print(f"Month {i}: payment is {payment}")
        difference = sum(differenceList) - int_principal
        print(f"Overpayment = {difference}")
    else:
        if parsed_arg[4] is None:
            int_principal = int(parsed_arg[1])
            int_periods = int(parsed_arg[2])
            float_interest = float(parsed_arg[3])

            i = float_interest / (12 * 100)
            numerator = i * math.pow(1 + i, int_periods)
            denominator = math.pow(1 + i, int_periods) - 1
            monthly_payment = math.ceil(int_principal * (numerator / denominator))
            print(f"Your annuity payment = {monthly_payment}!")
            difference = int_periods * monthly_payment - int_principal
            print(f"Overpayment = {difference}")
        elif parsed_arg[1] is None:
            int_payment = int(parsed_arg[4])
            int_periods = int(parsed_arg[2])
            float_interest = float(parsed_arg[3])
            i = float_interest / (12 * 100)
            numerator = i * math.pow(1 + i, int_periods)
            denominator = math.pow(1 + i, int_periods) - 1
            loan_principal = math.floor(int_payment / (numerator / denominator))
            print(f"Your loan principal = {loan_principal}!")
            difference = int_periods * int_payment - loan_principal
            print(f"Overpayment = {difference}")
        elif parsed_arg[2] is None:
            int_payment = int(parsed_arg[4])
            int_principal = int(parsed_arg[1])
            float_interest = float(parsed_arg[3])
            i = float_interest / (12 * 100)
            n = math.log(int_payment / (int_payment - i * int_principal), 1 + i)
            month = math.ceil(n)
            if month % 12 == 0:
                print(f"It will take {month // 12} years to repay this loan!")
            else:
                print(f"It will take {month // 12} years and {month % 12} months to repay this loan!")
            difference = month * int_payment - int_principal
            print(f"Overpayment = {difference}")




def calculator():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", )
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    parser.add_argument("--payment")
    args = parser.parse_args()

    type_arg = args.type
    principal_arg = args.principal
    periods_arg = args.periods
    interest_arg = args.interest
    payment_arg = args.payment

    parsed_args = [type_arg, principal_arg, periods_arg, interest_arg, payment_arg]

    if find_problems(parsed_args):
        return

    calculate(parsed_args)


calculator()
