COCOMO_MODES = {
    "1": {"name": "Organic", "a": 2.4, "b": 1.05, "c": 2.5, "d": 0.38},
    "2": {"name": "Semi-Detached", "a": 3.0, "b": 1.12, "c": 2.5, "d": 0.35},
    "3": {"name": "Embedded", "a": 3.6, "b": 1.20, "c": 2.5, "d": 0.32},
}


def calculate_cocomo():
    print("--- Basic COCOMO Estimator ---")
    print("Choose Project Mode:")
    print("1. Organic (Small teams, flexible requirements)")
    print("2. Semi-Detached (Medium teams, mixed experience)")
    print("3. Embedded (Tight constraints, highly complex)")

    mode_choice = input("Enter choice (1-3): ").strip()

    if mode_choice not in COCOMO_MODES:
        print("Invalid selection. Exiting program.")
        return

    try:
        kloc = float(input("Enter project size in KLOC (Kilo Lines of Code): "))
        if kloc <= 0:
            print("KLOC must be greater than 0.")
            return
    except ValueError:
        print("Invalid number entered for KLOC.")
        return

    mode = COCOMO_MODES[mode_choice]
    a, b, c, d = mode["a"], mode["b"], mode["c"], mode["d"]

    effort = a * (kloc**b)
    time = c * (effort**d)
    staff = effort / time

    print("\n--- Estimation Results ---")
    print(f"Selected Mode:    {mode['name']}")
    print(f"Project Size:     {kloc:.2f} KLOC")
    print(f"Effort Required:  {effort:.2f} Person-Months")
    print(f"Development Time: {time:.2f} Months")
    print(f"Persons Required: {staff:.2f} People")


if __name__ == "__main__":
    calculate_cocomo()
