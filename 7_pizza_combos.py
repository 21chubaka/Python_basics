'''
Pizza Topping Combos program:
Prompt the user for number of toppings set it to num_top.
Prompt the user for number of toppings on a standard pizza, set it to stand_top.
Intialize variables n_fac and k_fac and set to one.
Intialize n_k_fac and set it to num_top - stand_top
Check it num_top, stand_top, and n_k_fac are greater or equal to zero.
    set up three factorial loops for n, k, and (n-k)
Else, negative number inform user
Intialize variable combos and set to n_fac / (k_fac * n_k_fac)
Return results to user
'''
num_top = int(input('Number of toppings today: '))
stand_top = int(input('Number of toppings on Standard Pizza today: '))

n_fac = 1
k_fac = 1
n_k_fac = num_top - stand_top

if num_top >= 0 and stand_top >= 0 and n_k_fac >= 0:
    for i in range(1, num_top + 1):
        n_fac = num_top * i
    for j in range(1, stand_top + 1):
        k_fac = stand_top * j
    for k in range(1, n_k_fac + 1):
        n_k_fac = n_k_fac * k
else:
    print('That is a negative number. Please try again')

combos = n_fac / (k_fac * n_k_fac)

print('Number of combinations: ', combos)