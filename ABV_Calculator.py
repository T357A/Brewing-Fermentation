original_gravity = float(
    input("What is your OG (Original Gravity I.E 1.040) reading?: ")
)
final_gravity = float(input("What is your FG (Final Gravity I.E. 1.000) reading?: "))
# Formula for Alc/Vol
alc_by_vol = (
    76.08 * (original_gravity - final_gravity) / (1.775 - original_gravity)
) * (final_gravity / 0.794)
# Using string formating to limit to 2 decimal places
abv = "{:.2f}".format(alc_by_vol)
print("Your alcohol by volume or ABV is: " + abv + "%")
