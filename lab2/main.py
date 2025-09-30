import utilities

def main():
    radius_circle = float(input("Enter de radius of a circle in cm: "))
    circle_area = utilities.calculate_circle_area(radius_circle)
    print("The are of circle is: ",circle_area)
    radius_sphere = float(input("Enter radius of the sphere in cm: "))
    volume_sphere = utilities.calculate_sphere_volume(radius_sphere)
    print("The volume of the sphere is: ", volume_sphere)
    bmi = utilities.calculate_bmi()
    print("The Body Mass Index is: ",bmi)
    hypotenuse = utilities.calculate_hypotenuse()
    print("The Hypotenuse length of the right triangle is: ", hypotenuse)

if __name__ == '__main__':
    main()
