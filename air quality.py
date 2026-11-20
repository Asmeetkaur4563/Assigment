import numpy as np
import pandas as pd

# QIR - Quality Inspection and Reporting System

data = {
    "Product_ID": ["P101", "P102", "P103", "P104", "P105",
                   "P106", "P107", "P108", "P109", "P110"],
    "Measurement_mm": [10.2, 9.8, 10.1, 11.5, 9.5,
                       10.0, 10.4, 8.9, 10.3, 9.9]
}

df = pd.DataFrame(data)

# Quality tolerance limits
LOWER_LIMIT = 9.0
UPPER_LIMIT = 11.0

def inspect_products():
    df["Status"] = np.where(
        (df["Measurement_mm"] >= LOWER_LIMIT) &
        (df["Measurement_mm"] <= UPPER_LIMIT),
        "PASS",
        "FAIL"
    )

def add_product():
    product_id = input("Enter Product ID: ")
    try:
        measurement = float(input("Enter measurement (mm): "))
        new_row = pd.DataFrame({
            "Product_ID": [product_id],
            "Measurement_mm": [measurement]
        })
        global df
        df = pd.concat([df, new_row], ignore_index=True)
        inspect_products()
        print("Product added successfully!")
    except ValueError:
        print("Please enter a valid numeric measurement.")

def show_records():
    inspect_products()
    print("\n--- Product Inspection Records ---")
    print(df.to_string(index=False))

def quality_analysis():
    inspect_products()

    measurements = df["Measurement_mm"].to_numpy()
    total = len(df)
    passed = (df["Status"] == "PASS").sum()
    failed = (df["Status"] == "FAIL").sum()

    if total == 0:
        print("No product records available.")
        return

    pass_rate = (passed / total) * 100
    defect_rate = (failed / total) * 100

    print("\n========== QIR QUALITY REPORT ==========")
    print(f"Total Products       : {total}")
    print(f"Passed Products      : {passed}")
    print(f"Failed Products     : {failed}")
    print(f"Quality Pass Rate   : {pass_rate:.2f}%")
    print(f"Defect Rate        : {defect_rate:.2f}%")
    print("-------------------------------------")
    print(f"Average Measurement: {np.mean(measurements):.2f} mm")
    print(f"Maximum Measurement: {np.max(measurements):.2f} mm")
    print(f"Minimum Measurement: {np.min(measurements):.2f} mm")
    print(f"Std. Deviation    : {np.std(measurements):.2f} mm")

    if defect_rate <= 5:
        print("Quality Level: GOOD")
    elif defect_rate <= 15:
        print("Quality Level: NEEDS IMPROVEMENT")
    else:
        print("Quality Level: POOR")

    print("=====================================")

def show_defects():
    inspect_products()
    defects = df[df["Status"] == "FAIL"]

    print("\n--- Defective Products ---")
    if defects.empty:
        print("No defective products found!")
    else:
        print(defects.to_string(index=False))

def export_report():
    inspect_products()
    df.to_csv("quality_report.csv", index=False)
    print("\nReport saved as quality_report.csv")

def main():
    inspect_products()

    while True:
        print("\n========== QIR QUALITY SYSTEM ==========")
        print("1. View Product Records")
        print("2. Add New Product")
        print("3. Quality Analysis Report")
        print("4. View Defective Products")
        print("5. Export CSV Report")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_records()
        elif choice == "2":
            add_product()
        elif choice == "3":
            quality_analysis()
        elif choice == "4":
            show_defects()
        elif choice == "5":
            export_report()
        elif choice == "6":
            print("Thank you for using QIR Quality System!")
            break
        else:
            print("Invalid choice! Please select from 1 to 6.")

if __name__ == "__main__":
    main()
