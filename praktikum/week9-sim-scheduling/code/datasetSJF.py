# Dataset
processes = ["P4", "P1", "P3", "P2"]
arrival_time = [3, 0, 2, 1]
burst_time = [3, 6, 7, 8]

n = len(processes)

start_time = [0] * n
finish_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n

# Penjadwalan 
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
print("Proses Burst Time Arrival Time Start Time Finish Time WT TAT")
for i in range(n):
    print(f"{processes[i]:<8}{burst_time[i]:<12}{arrival_time[i]:<14}"
          f"{start_time[i]:<12}{finish_time[i]:<13}"
          f"{waiting_time[i]:<6}{turnaround_time[i]:<6}")

print(f"\nRata-rata Waiting Time     = {round(avg_waiting_time, 1)}")
print(f"Rata-rata Turnaround Time  = {round(avg_turnaround_time, 1)}")
