from shapemanager import ShapeManager

def main():
    start = input("Do you want to start the shape manager? (yes/no): ").strip().lower()
    if start != "yes":
        print("Goodbye!")
        return

    manager = ShapeManager()

    while True:
        print("\nMenu:")
        print("1. Add new shape")
        print("2. List all shapes")
        print("3. Sum all circumferences")
        print("4. Sum all areas")
        print("5. Find biggest circumference")
        print("6. Find biggest area")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            manager.add_shape()
        elif choice == "2":
            manager.list_all_shapes()
        elif choice == "3":
            manager.sum_all_circumferences()
        elif choice == "4":
            manager.sum_all_areas()
        elif choice == "5":
            manager.find_biggest_circumference()
        elif choice == "6":
            manager.find_biggest_area()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
