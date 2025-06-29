# src/report_writer.py

import pandas as pd

def save_report(results, filename="results/report.csv"):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"[✓] Report saved to {filename}")
