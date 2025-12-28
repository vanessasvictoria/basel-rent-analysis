from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = Path("data/processed/sample_listings.csv")
OUT_DIR = Path("outputs/figures")

def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    df["rent_per_m2"] = df["price_chf"] / df["size_m2"]

    # 1) Rent distribution
    plt.figure()
    df["price_chf"].plot(kind="hist", bins=8)
    plt.title("Basel Rent Distribution (CHF/month)")
    plt.xlabel("Rent (CHF)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "rent_distribution.png")
    plt.close()

    # 2) Rent per m² distribution
    plt.figure()
    df["rent_per_m2"].plot(kind="hist", bins=8)
    plt.title("Rent per m² Distribution (CHF)")
    plt.xlabel("CHF per m²")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "rent_per_m2_distribution.png")
    plt.close()

    # 3) Price vs size
    plt.figure()
    plt.scatter(df["size_m2"], df["price_chf"])
    plt.title("Price vs Size")
    plt.xlabel("Size (m²)")
    plt.ylabel("Rent (CHF/month)")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "price_vs_size.png")
    plt.close()

    print("Saved figures to outputs/figures/")

if __name__ == "__main__":
    main()
