# main.py - simple summary script for the healthcare starter dataset
import pandas as pd

def load_data(path='data'):
    patients = pd.read_csv(f'{path}/patients.csv')
    appts = pd.read_csv(f'{path}/appointments.csv')
    billing = pd.read_csv(f'{path}/billing.csv')
    return patients, appts, billing

def summarize():
    patients, appts, billing = load_data('data')
    report = []
    report.append(f'Total patients: {patients["patient_id"].nunique()}')
    report.append(f'Total appointments: {len(appts)}')
    completed = appts[appts["status"]=="Completed"]
    report.append(f'Completed appointments: {len(completed)}')
    revenue = billing["total_amount"].sum()
    report.append(f'Total billed amount: {revenue}')
    top_depts = appts["department_id"].value_counts().head(5).to_dict()
    report.append("Top departments (by appointments):")
    for k,v in top_depts.items():
        report.append(f'  {k}: {v} appts')
    with open("summary_report.txt","w") as f:
        f.write('\n'.join(report))
    print('\n'.join(report))

if __name__ == "__main__":
    summarize()
