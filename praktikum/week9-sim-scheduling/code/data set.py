# Dataset
processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 2, 3]
burst_time = [6, 8, 7, 3]

n = len(processes)

start_time = [0] * n
finish_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n

# FCFS Scheduling
for i in range(n):
    if i == 0:
        start_time[i] = arrival_time[i]
    else:
        start_time[i] = max(finish_time[i - 1], arrival_time[i])

    finish_time[i] = start_time[i] + burst_time[i]

    waiting_time[i] = start_time[i] - arrival_time[i]
    turnaround_time[i] = finish_time[i] - arrival_time[i]

# Hitung rata-rata
avg_waiting_time = sum(waiting_time) / n
avg_turnaround_time = sum(turnaround_time) / n

# Tampilkan hasil
print("Proses Arrival Burst Time Start Time Finish Time Waiting Time Turnaround")
for i in range(n):
    print(f"{processes[i]:<8}{burst_time[i]:<12}{arrival_time[i]:<14}"
          f"{start_time[i]:<12}{finish_time[i]:<13}"
          f"{waiting_time[i]:<6}{turnaround_time[i]:<6}")

print("\nRata-rata Waiting Time     =", round(avg_waiting_time, 2))
print("Rata-rata Turnaround Time =", round(avg_turnaround_time, 2))
