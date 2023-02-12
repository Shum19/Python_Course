import os, random;
os.system('clear')
bushes_quantities = int(input("Input the number of bushes - "));
# berries_quantities = [ 1, 2, 3, 4]
berries_quantities = [random.randint(1, 30) for i in range(bushes_quantities)];
print(f"{bushes_quantities} -> {berries_quantities}");
max_berries = 0;
for i in range(1, bushes_quantities - 1):
    temp_max = berries_quantities[i] + berries_quantities[i - 1] + berries_quantities[i + 1]
    if temp_max > max_berries:
        position = (f'best position between bushes №{i} and №{i + 2}\nP.S. Starts count'
                    ' bushes number from 1');
        max_berries = temp_max;
print(f'{max_berries} are maximum berries at ', position);