from math import ceil, log, floor
import argparse
import sys

ap = argparse.ArgumentParser()
ap.add_argument("--type", help="annuity or diff")
ap.add_argument("--principal", type=int)
ap.add_argument("--periods", type=int)
ap.add_argument("--interest", type=float)
ap.add_argument("--payment", type=int)

args = vars(ap.parse_args())

count = 0
for v in args.values():
    if v is None:
        count += 1

if count > 1:
    print("Incorrect parameters.")
    sys.exit()
elif args['payment'] and args['type'] == "diff":
    print("Incorrect parameters")
    sys.exit()
elif args['type'] != "annuity" and args['type'] != "diff":
    print("Incorrect parameters")
    sys.exit()
elif args['type'] == "annuity" and args['principal'] and args['payment'] and args['periods']:
    print("Incorrect parameters")
    sys.exit()
else:
    ans = args['type']

    if not args['principal']:
        c_principal = 0
    else:
        c_principal = args['principal']
    if not args['periods']:
        c_periods = 0
    else:
        c_periods = args['periods']
    c_interest = args['interest']
    if not args['payment']:
        monthly_payment = 0
    else:
        monthly_payment = args['payment']

    if ans == "diff" and args['principal'] and args['periods'] and args['interest']:
        if args['interest'] < 0 or args['principal'] <= 0 or args['periods'] <= 0:
            print("Incorrect parameters")
            sys.exit()
        else:
            c_interest = c_interest / (12 * 100)
            total = 0
            for i in range(1, c_periods + 1):
                month_total = (c_principal / c_periods) + c_interest * (c_principal - ((c_principal * (i-1)) / c_periods))
                print(f'Month {i}: paid out {ceil(month_total)}')
                total += ceil(month_total)
            print()
            print(f'Overpayment = {total - c_principal}')
    elif ans == "annuity" and args['principal'] and args['periods'] and args['interest']:
        if args['interest'] < 0 or args['principal'] <= 0 or args['periods'] <= 0:
            print("Incorrect parameters")
            sys.exit()
        else:
            c_interest = c_interest / (12 * 100)
            annuity = c_principal *((c_interest * (1 + c_interest) ** c_periods) / (((1 + c_interest) ** c_periods) - 1))
            print(f'Your annuity payment = {ceil(annuity)}!')
            total = 0
            for i in range(1, c_periods + 1):
                month_total = (c_principal / c_periods) + c_interest * (c_principal - ((c_principal * (i-1)) / c_periods))
                total += ceil(month_total)
            print(f'Overpayment = {(ceil(annuity) * c_periods) - c_principal}')
    elif ans == "annuity" and args['payment'] and args['periods'] and args['interest']:
        if args['interest'] < 0 or args['payment'] < 0 or args['periods'] <= 0:
            print("Incorrect parameters")
            sys.exit()
        else:
            c_interest_dec = c_interest / (12 * 100)
            c_principal = monthly_payment / ((c_interest_dec * (1 + c_interest_dec) ** c_periods) / (((1 + c_interest_dec) ** c_periods) - 1))
            print("Your credit principal = " + str(floor(c_principal)) + "!")
            print(f'Overpayment = {ceil((monthly_payment * c_periods) - c_principal)}')
    elif ans == "annuity" and args['principal'] and args['payment'] and args['interest']:
        if args['interest'] < 0 or args['principal'] <= 0 or args['payment'] < 0:
            print("Incorrect parameters")
            sys.exit()
        else:
            c_interest_dec = c_interest / (12 * 100)
            n = log((monthly_payment / (monthly_payment - c_interest_dec * c_principal)), (1 + c_interest_dec))
            n = ceil(n)
            if 12 > n > 1:
                print(f"You need {str(n)} months to repay this credit!")
            elif n == 1:
                print(f"You need 1 month to repay this credit!")
            elif n % 12 == 0:
                year = n / 12
                if year == 1:
                    print(f"You need 1 year to repay this credit!")
                else:
                    print(f"You need {str(int(year))} years to repay this credit!")
            else:
                year = n // 12
                months = n % 12
                if year == 1 and months == 1:
                    print(f"You need 1 year and 1 month to repay this credit!")
                elif year == 1 and months > 1:
                    print(f"You need 1 year and {str(months)} months to repay this credit!")
                elif year > 1 and months == 1:
                    print(f"You need {str(year)} years and 1 month to repay this credit!")
                elif year > 1 and months > 1:
                    print(f"You need {str(year)} years and {str(months)} months to repay this credit!")
            print(f"Overpayment = {(n * monthly_payment) - c_principal}")
