def last_not_this_yr(last_yr_donors,this_yr_donors):
    # To find list of donors who gave last year but not this year:
    donors_difference = last_yr_donors.difference(this_yr_donors)
    return sorted(list(donors_difference))

def both_yrs(last_yr_donors,this_yr_donors):
    # To find list of donors who gave both years:
    donors_intersection = last_yr_donors.intersection(this_yr_donors)
    return sorted(list(donors_intersection))

def this_not_last_yr(last_yr_donors,this_yr_donors):
    # To find list of donors who gave this year but not last year:
    donors_difference = this_yr_donors.difference(last_yr_donors)
    return sorted(list(donors_difference))

def main():
    # To act as __main__ function + take in donors based on input format + output resulting data:
    n = int(input())
    output = []
    for i in range(0,n):
        last_yr_donors = set()
        this_yr_donors = set()
        last_yr_donors.update(input().split(','))
        this_yr_donors.update(input().split(','))
        output.append(last_not_this_yr(last_yr_donors,this_yr_donors))
        output.append(both_yrs(last_yr_donors,this_yr_donors))
        output.append(this_not_last_yr(last_yr_donors,this_yr_donors))
    
    for item in output:
        print(','.join(item))
        
main()
